from flask import Blueprint, render_template, request, redirect, session, abort
import secrets
from markupsafe import escape
from database import get_db_connection

secure_bp = Blueprint("secure", __name__)

@secure_bp.route("/", methods=["GET", "POST"])
def notes():
    conn = get_db_connection()
    
    # [SAVUNMA] CSRF Koruması için benzersiz token üretimi
    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_hex(16)
        
    if request.method == "POST":
        # 1. CSRF Kontrolü: Formdan gelen token ile oturumdaki token eşleşmeli
        submitted_token = request.form.get("csrf_token")
        if not submitted_token or submitted_token != session.get("csrf_token"):
            abort(403) # Yetkisiz erişim hatası döndür
            
        # 2. [HUKUKİ UYUM] KVKK Onay Kontrolü
        # Kullanıcı checkbox'ı işaretlemediyse veri işleme sürecini durdurur
        kvkk_consent = request.form.get("kvkk_consent")
        if not kvkk_consent:
            return "HATA: KVKK aydınlatma metnini onaylamadan veri kaydedilemez.", 400

        content = request.form.get("content")
        author = request.form.get("author")
        
        # 3. [SAVUNMA] Input Sanitization (XSS Koruması)
        # Girdilerdeki zararlı HTML/JS karakterleri düz metne dönüştürülür
        clean_content = escape(content)
        clean_author = escape(author)
        
        # 4. [SAVUNMA] Prepared Statements (SQL Injection Koruması)
        # Veri, sorgu iskeletinden ayrı olarak güvenli bir şekilde gönderilir
        query = "INSERT INTO notes (content, author) VALUES (?, ?)"
        
        try:
            # Parametreli sorgu kullanımı
            conn.execute(query, (clean_content, clean_author)) 
            conn.commit()
        except Exception as e:
            print("Veritabanı hatası:", e)
            
        return redirect("/secure/")
        
    # GET isteğinde verileri güvenli şekilde çek ve sayfaya gönder
    notes = conn.execute("SELECT * FROM notes ORDER BY id DESC").fetchall()
    conn.close()
    
    return render_template("secure.html", notes=notes, csrf_token=session["csrf_token"])

@secure_bp.route("/forget", methods=["POST"])
def forget():
    # 1. [SAVUNMA] CSRF Kontrolü
    submitted_token = request.form.get("csrf_token")
    if not submitted_token or submitted_token != session.get("csrf_token"):
        abort(403)
        
    author_to_delete = request.form.get("author")
    if not author_to_delete:
        return "HATA: Silinecek isim belirtilmedi.", 400

    conn = get_db_connection()
    
    # 2. [HUKUKİ UYUM & SAVUNMA] Unutulma Hakkı + Prepared Statement
    # Kullanıcının adıyla eşleşen TÜM verileri kalıcı olarak siler
    query = "DELETE FROM notes WHERE author = ?"
    
    try:
        conn.execute(query, (author_to_delete,))
        conn.commit()
    except Exception as e:
        print("Veritabanı hatası:", e)
    finally:
        conn.close()
        
    return redirect("/secure/")

import json
from flask import Response

@secure_bp.route("/download", methods=["POST"])
def download():
    # 1. [SAVUNMA] CSRF Kontrolü
    submitted_token = request.form.get("csrf_token")
    if not submitted_token or submitted_token != session.get("csrf_token"):
        abort(403)
        
    author_to_download = request.form.get("author")
    if not author_to_download:
        return "HATA: Kullanıcı adı belirtilmedi.", 400

    conn = get_db_connection()
    
    # 2. [SAVUNMA & HUKUKİ UYUM] Parametreli Sorgu ile Sadece Kullanıcının Verilerini Çekme
    query = "SELECT id, author, content FROM notes WHERE author = ?"
    
    try:
        rows = conn.execute(query, (author_to_download,)).fetchall()
        
        # Gelen veriyi JSON formatına uygun sözlük listesine dönüştür
        user_data = [
            {"not_id": row["id"], "yazar": row["author"], "not_icerigi": row["content"]} 
            for row in rows
        ]
        
        # JSON verisini string'e çevir (Türkçe karakterleri korumak için ensure_ascii=False)
        json_output = json.dumps(user_data, ensure_ascii=False, indent=4)
        
        # 3. Tarayıcıya dosyayı indirmesi talimatını veren Response nesnesi döndür
        return Response(
            json_output,
            mimetype="application/json",
            headers={"Content-Disposition": f"attachment; filename={author_to_download}_veri_paketi.json"}
        )
        
    except Exception as e:
        print("Veritabanı hatası:", e)
        return "Veri çekme işlemi sırasında bir hata oluştu.", 500
    finally:
        conn.close()
