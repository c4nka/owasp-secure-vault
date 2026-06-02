# 💉 SQL Injection (SQLi) Anatomisi ve Savunma Mimarisi

Bu doküman, projede uygulanan **SQL Injection (SQLi)** zafiyetinin nasıl çalıştığını, potansiyel etkilerini ve güvenli rotada (`/secure`) bu zafiyetin nasıl kapatıldığını teknik olarak açıklar.

## 1. SQL Injection Nedir?

SQL Injection, saldırganların bir web uygulamasının veritabanı sorgularına müdahale etmesini sağlayan kritik bir güvenlik açığıdır. Saldırgan, kullanıcı girdisi alanlarına (örneğin, bir arama kutusu veya giriş formu) zararlı SQL komutları ekleyerek veritabanındaki verilere yetkisiz erişim sağlayabilir, verileri değiştirebilir veya silebilir.

## 2. Zafiyetli Senaryo (Vulnerable Route)

Zafiyetli rotada (`/vulnerable`), kullanıcılardan alınan notlar ve yazar isimleri hiçbir filtrelemeden geçirilmeden, doğrudan string birleştirme (string concatenation) yöntemiyle SQL sorgusuna eklenir.

### 💥 İstismar (Exploitation) Örneği

Saldırgan, "Yazar Adı" alanına şu payload'u girer:

```sql
Ahmet', 'Zararlı İçerik'); DROP TABLE notes; --
```

## 🔍 Neden Çalışır?
Arka planda çalışan SQL sorgusu şu şekildedir:

```sql
INSERT INTO notes (author, content) VALUES ('" + yazar_adi + "', '" + not_icerigi + "')
```

Saldırganın girdisi eklendiğinde sorgu şu hale gelir:

```sql
INSERT INTO notes (author, content) VALUES ('Ahmet', 'Zararlı İçerik'); DROP TABLE notes; --', 'Herhangi bir not')
```

Bu durumda veritabanı, önce INSERT işlemini yapar, ardından noktalı virgül (;) ile ayrılmış olan DROP TABLE notes komutunu çalıştırarak tüm tabloyu siler. -- kısmı ise sorgunun geri kalanını yorum satırı haline getirerek hata alınmasını engeller.

## 3. Güvenli Senaryo ve Savunma (Secure Route)
Güvenli rotada (/secure), SQL Injection saldırılarını tamamen engellemek için Prepared Statements (Parametreli Sorgular) kullanılmıştır.

## 🛡️ Savunma Mekanizması: Prepared Statements
Kullanıcıdan alınan veriler, doğrudan SQL sorgusuna eklenmek yerine, sorguda yer tutucular (genellikle ? veya %s) kullanılarak veritabanına gönderilir. Veriler, sorgudan ayrı bir parametre olarak iletilir.

```
# Kullanıcı girdisi parametreli sorgu (Prepared Statement) ile veritabanına iletilir
query = "INSERT INTO notes (content, author) VALUES (?, ?)"
conn.execute(query, (clean_content, clean_author))
```

## Neden Güvenlidir?
Prepared Statements kullanıldığında, veritabanı sürücüsü (örneğin SQLite veya PostgreSQL), kullanıcı girdisini çalıştırılabilir SQL komutları olarak değil, sadece "veri" (string) olarak kabul eder. Saldırganın girdiği DROP TABLE gibi zararlı komutlar çalıştırılmaz, sadece yazar adının bir parçası olarak veritabanına kaydedilir.

## 4. Etki ve Sonuç
Uygulanan Prepared Statements yöntemi sayesinde:

-- Veritabanındaki verilerin yetkisiz okunması, değiştirilmesi veya silinmesi (Data Breach) engellenmiştir.

-- SQL sorgularına müdahale edilerek sistem üzerinde komut çalıştırılması (RCE) riski ortadan kaldırılmıştır.

-- Veri bütünlüğü ve gizliliği tam olarak sağlanmıştır.
