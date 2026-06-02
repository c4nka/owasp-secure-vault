# Research Notes / Araştırma Notları

> Module / Konu: Hukuki Regülasyonların (KVKK) Güvenli Kodlamaya Entegrasyonu
> Date / Tarih: 2026-06-02

---

## What I'm Investigating / Araştırdığım Konu

Bir web uygulamasında OWASP Top 10 zafiyetlerini kapatmanın ötesine geçerek, veri mahremiyeti yasalarının (KVKK Madde 7 ve Madde 11) Flask ve SQLite mimarisine teknik olarak nasıl gömülebileceğini ve bu süreçte adli bilişim loglarının (ISO 27001) nasıl tutulacağını araştırıyorum.

## Resources Found / Bulunan Kaynaklar

- [KVKK Mevzuatı ve Kararları](https://www.kvkk.gov.tr/) — Veri sorumlusunun yükümlülükleri ve veri sahibinin haklarının hukuki çerçevesini öğrendim.
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) — "Right to be Forgotten" uygulanırken veritabanı silme işlemlerinde SQL Injection'dan korunmak için Prepared Statement'ların zorunlu olduğunu doğruladım.
- [Python Logging Documentation](https://docs.python.org/3/library/logging.html) — Değiştirilemez ve zaman damgalı denetim izlerinin (audit logs) nasıl yapılandırılacağını öğrendim.

## Key Findings / Temel Bulgular

1. Gerçek güvenlik sadece teknik saldırıları (XSS, SQLi) engellemek değildir; aynı zamanda kullanıcıya verisi üzerinde kontrol hakkı vererek hukuki riskleri (Compliance) sıfırlamaktır.
2. Unutulma hakkı kapsamında veri silinirken, sistem loglarının (audit.log) silinmemesi gerekir. Loglar, sistemin değil işlemin kanıtıdır ve adli/idari uyuşmazlıklarda esastır.

## Dead Ends / Çıkmaz Sokaklar

- **Ham SQL Sorgusu ile Silme Denemesi:** `DELETE FROM notes WHERE author = ' + user_input + '` şeklinde denendi → **Başarısız oldu.** SQL Injection zafiyeti doğurduğu için iptal edildi. Yerine `?` parametreli güvenli sorgu yapısı kuruldu.
- **Logların Veritabanında Tutulması:** Uygulama loglarını SQLite tablosuna yazmak denendi → **Vazgeçildi.** Veritabanı ele geçirilirse loglar da silinebileceği için loglar dışa aktarılarak bağımsız bir `audit.log` dosyasına yönlendirildi (Defense in Depth).

## Questions Remaining / Kalan Sorular

- [x] JSON formatında dışa aktarılan veriler şifrelenmeli mi? (Şu an standart JSON formatında çıkıyor, ileride GPG ile şifrelenebilir).
- [ ] Log dosyasının boyutu çok büyüdüğünde otomatik arşivleme (log rotation) nasıl yapılabilir?

## 50-Step Breakdown / 50 Adımlık Çözümleme (Özet)

1. Step 1: KVKK Madde 7 teknik olarak ne anlama geliyor? (Veritabanından DELETE işlemi)
2. Step 2: Hangi veri tabanı tabloları kişisel veri barındırıyor? (notes tablosu)
3. Step 3: Silme işlemi için arayüzde nasıl bir form olmalı? (CSRF korumalı POST formu)
4. Step 4: Kullanıcı girdisi silme sorgusuna nasıl güvenli aktarılır? (Prepared Statements)
5. Step 5: İşlem başarısı nasıl kayıt altına alınır? (Python logging kütüphanesi)
*(Araştırma tasarımı gereği temel adımlar kurgulanmış, uygulama aşamasında kodlara dökülmüştür.)*
