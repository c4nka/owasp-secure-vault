# Modül Adı / Module Name: KVKK & GDPR Compliance Engine

## Amaç / Purpose

Bu modül, uygulamaya kayıt olan kullanıcıların verileri üzerinde KVKK Madde 7 (Unutulma Hakkı) ve Madde 11 (Veri Taşınabilirliği) kapsamındaki yasal haklarını teknik olarak, SQL Injection risklerinden arındırılmış bir şekilde kullanabilmelerini sağlar.

## Nasıl Çalışır / How It Works

1. **Unutulma Hakkı (Right to be Forgotten):** Kullanıcı arayüzden `/secure/forget` uç noktasına talep gönderir. Sistem, CSRF doğrulamasını geçtikten sonra `Prepared Statements` kullanarak veritabanındaki (SQLite) ilgili kullanıcıya ait tüm kayıtları kalıcı olarak siler (`DELETE FROM notes WHERE author = ?`).
2. **Veri Taşınabilirliği (Data Portability):** Kullanıcı `/secure/download` uç noktasına istek attığında, sistem sadece o kullanıcıya ait verileri filtreler.
3. **Yapılandırma (Structuring):** Çekilen ham veriler, makinece okunabilir uluslararası bir standart olan JSON formatına dönüştürülerek kullanıcıya şifreli tünel üzerinden indirilir.

## Kullanım / Usage

Modül, Flask uygulamasının web arayüzü üzerinden tetiklenir. Kullanıcı etkileşimi şu şekildedir:
- **Veri Silme:** Kusursuz Kasa > "Verilerimi Kalıcı Olarak Sil" butonu.
- **Veri İndirme:** Kusursuz Kasa > "Verilerimi JSON Olarak İndir" butonu.

## Çıktı / Output

- **Silme İşlemi Çıktısı:** İşlem başarılı olduğunda veritabanı kayıtları yok edilir ve `audit.log` dosyasına ISO 27001 uyumlu bir denetim izi bırakılır.
- **İndirme İşlemi Çıktısı:** Kullanıcının bilgisayarına `[KullanıcıAdı]_veri_paketi.json` adında, `{"not_id": 1, "yazar": "X", "not_icerigi": "Y"}` formatında yapılandırılmış bir veri seti indirilir.

## Bilinen Kısıtlamalar / Known Limitations

- ISO 27001 izlenebilirlik standartları gereği, kullanıcı veritabanından silinse bile `audit.log` içindeki eylem kaydı (kimin, ne zaman silme talebi gönderdiği) hukuki delil niteliği taşıdığı için silinmez.
