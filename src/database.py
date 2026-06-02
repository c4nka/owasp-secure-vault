import sqlite3

DB_NAME = "vault.db"

def get_db_connection():
    """Veritabanına bağlanır ve bağlantı nesnesini döndürür."""
    conn = sqlite3.connect(DB_NAME)
    # Verileri dict (sözlük) formatında kolayca çekebilmek için:
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Veritabanını ve gerekli tabloları oluşturur."""
    conn = get_db_connection()
    
    # Notların tutulacağı tabloyu oluştur
    conn.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            author TEXT NOT NULL
        )
    ''')
    
    # Test için tablo boşsa örnek bir veri ekleyelim
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM notes")
    if cursor.fetchone()[0] == 0:
        conn.execute(
            "INSERT INTO notes (content, author) VALUES ('Sisteme hoş geldiniz. Bu ilk nottur.', 'Admin')"
        )
        
    conn.commit()
    conn.close()
    print(f"[*] Veritabanı '{DB_NAME}' başarıyla başlatıldı ve tablolar oluşturuldu.")

if __name__ == "__main__":
    # Bu dosya doğrudan çalıştırılırsa veritabanını kur
    init_db()
