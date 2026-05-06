# Temel alınacak hafif Python imajı
FROM python:3.10-slim

# Konteyner içindeki çalışma dizinimiz
WORKDIR /app

# Önce sadece requirements.txt'yi kopyala (Docker önbelleğini verimli kullanmak için)
COPY requirements.txt .

# Bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# Projenin geri kalan tüm dosyalarını kopyala
COPY . .

# Konteyner ayağa kalkarken veritabanını otomatik oluştur
RUN python database.py

# Flask'ın çalışacağı 5000 portunu dışa aç
EXPOSE 5000

# Uygulamayı başlat
CMD ["python", "app.py"]
