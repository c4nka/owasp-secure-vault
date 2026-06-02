from flask import Blueprint, render_template, request, redirect
from database import get_db_connection

vul_bp = Blueprint("vulnerable", __name__)

@vul_bp.route("/", methods=["GET", "POST"])
def notes():
    conn = get_db_connection()
    
    if request.method == "POST":
        content = request.form.get("content")
        author = request.form.get("author")
        
        # [!] ZAFİYET 1: SQL Injection (SQLi)
        # Girdi hiçbir filtrelemeden geçmeden doğrudan string birleştirme (f-string) ile SQL'e yazılıyor!
        # Parametreli sorgu (Prepared Statement) KULLANILMADIĞI için tehlikeli.
        query = f"INSERT INTO notes (content, author) VALUES ('{content}', '{author}')"
        
        try:
            conn.executescript(query) 
            conn.commit()
        except Exception as e:
            print("Veritabanı hatası:", e)
            
        return redirect("/vulnerable/")
        
    # GET isteği: Veritabanındaki notları çek ve sayfaya gönder
    notes = conn.execute("SELECT * FROM notes ORDER BY id DESC").fetchall()
    conn.close()
    
    return render_template("vulnerable.html", notes=notes)
