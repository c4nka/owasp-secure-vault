from flask import Blueprint, render_template, request, redirect, session, abort, Response
import secrets
import json
import logging
from markupsafe import escape
from database import get_db_connection

secure_bp = Blueprint("secure", __name__)

# [ISO 27001 UYUM] Denetim İzi (Audit Logger) Yapılandırması
logging.basicConfig(
    filename="audit.log",
    level=logging.INFO,
    format="%(asctime)s - [DENETIM IZI] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

@secure_bp.route("/", methods=["GET", "POST"])
def notes():
    conn = get_db_connection()
    
    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_hex(16)
        
    if request.method == "POST":
        submitted_token = request.form.get("csrf_token")
        if not submitted_token or submitted_token != session.get("csrf_token"):
            logging.warning("YETKISIZ ERISIM: Gecersiz veya eksik CSRF Token ile istek atildi!")
            abort(403)
            
        kvkk_consent = request.form.get("kvkk_consent")
        if not kvkk_consent:
            logging.warning("KVKK IHLALI: Kullanici rıza kutusunu isaretlemeden veri gondermeyi denedi.")
            return "HATA: KVKK aydınlatma metnini onaylamadan veri kaydedilemez.", 400

        content = request.form.get("content")
        author = request.form.get("author")
        
        clean_content = escape(content)
        clean_author = escape(author)
        
        query = "INSERT INTO notes (content, author) VALUES (?, ?)"
        
        try:
            conn.execute(query, (clean_content, clean_author)) 
            conn.commit()
            # [LOGLAMA] Başarılı veri ekleme kaydı
            logging.info(f"Kullanici: '{clean_author}' tarafından sisteme yeni bir not eklendi. Durum: BASARILI.")
        except Exception as e:
            logging.error(f"VERITABANI HATASI: Not ekleme sirasinda hata olustu: {str(e)}")
            print("Veritabanı hatası:", e)
            
        return redirect("/secure/")
        
    notes = conn.execute("SELECT * FROM notes ORDER BY id DESC").fetchall()
    conn.close()
    
    return render_template("secure.html", notes=notes, csrf_token=session["csrf_token"])

@secure_bp.route("/forget", methods=["POST"])
def forget():
    submitted_token = request.form.get("csrf_token")
    if not submitted_token or submitted_token != session.get("csrf_token"):
        logging.warning("YETKISIZ ERISIM: Gecersiz CSRF ile Unutulma Hakki tetiklenmeye calisildi!")
        abort(403)
        
    author_to_delete = request.form.get("author")
    if not author_to_delete:
        return "HATA: Silinecek isim belirtilmedi.", 400

    conn = get_db_connection()
    query = "DELETE FROM notes WHERE author = ?"
    
    try:
        conn.execute(query, (author_to_delete,))
        conn.commit()
        # [LOGLAMA] Başarılı veri silme (Unutulma Hakkı) kaydı
        logging.info(f"KVKK MADDE 7: '{author_to_delete}' talebiyle ait tüm veriler sistemden kalıcı olarak silindi. Durum: BASARILI.")
    except Exception as e:
        logging.error(f"VERITABANI HATASI: Unutulma hakki islemi sirasinda hata olustu: {str(e)}")
    finally:
        conn.close()
        
    return redirect("/secure/")

@secure_bp.route("/download", methods=["POST"])
def download():
    submitted_token = request.form.get("csrf_token")
    if not submitted_token or submitted_token != session.get("csrf_token"):
        logging.warning("YETKISIZ ERISIM: Gecersiz CSRF ile Veri Tasinabilirligi tetiklenmeye calisildi!")
        abort(403)
        
    author_to_download = request.form.get("author")
    if not author_to_download:
        return "HATA: Kullanıcı adı belirtilmedi.", 400

    conn = get_db_connection()
    query = "SELECT id, author, content FROM notes WHERE author = ?"
    
    try:
        rows = conn.execute(query, (author_to_download,)).fetchall()
        user_data = [
            {"not_id": row["id"], "yazar": row["author"], "not_icerigi": row["content"]} 
            for row in rows
        ]
        
        json_output = json.dumps(user_data, ensure_ascii=False, indent=4)
        
        # [LOGLAMA] Başarılı veri dışa aktarma (Veri Taşınabilirliği) kaydı
        logging.info(f"KVKK MADDE 11: '{author_to_download}' talebiyle veri paketi disasa aktarildi (JSON Export). Durum: BASARILI.")
        
        return Response(
            json_output,
            mimetype="application/json",
            headers={"Content-Disposition": f"attachment; filename={author_to_download}_veri_paketi.json"}
        )
        
    except Exception as e:
        logging.error(f"VERITABANI HATASI: Veri indirme islemi sirasinda hata olustu: {str(e)}")
        return "Veri çekme işlemi sırasında bir hata oluştu.", 500
    finally:
        conn.close()
