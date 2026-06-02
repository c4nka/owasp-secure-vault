# Research Notes / Araştırma Notları

> Module / Konu: Hukuki İçtihatlar, KVKK Kurul Kararları ve Adli Bilişim Standartları (ISO 27001)
> Date / Tarih: 2026-06-02

---

## What I'm Investigating / Araştırdığım Konu

Bu araştırmanın amacı, geliştirdiğimiz "Kusursuz Kasa" uygulamasındaki hukuki uyumluluk modüllerinin (Veri Taşınabilirliği, Unutulma Hakkı ve Denetim İzi) gerçek dünyadaki yasal karşılıklarını incelemektir. Özellikle veri sızıntılarında (SQLi gibi) ve veri silme taleplerinin ihlalinde KVKK Kurumu'nun verdiği idari para cezası emsallerini ve `audit.log` dosyamızın dijital mahkemelerde nasıl bir delil (Digital Forensics) niteliği taşıdığını araştırıyorum.

## Resources Found / Bulunan Kaynaklar

- [KVKK Kurul Kararları Özeti (İdari Para Cezaları)](https://www.kvkk.gov.tr/Icerik/5362/Kurul-Kararlari) — Şirketlerin "Yeterli teknik ve idari tedbiri almaması" (Madde 12) sebebiyle yediği cezaların resmi arşivi.
- [5651 Sayılı İnternet Ortamında Yapılan Yayınların Düzenlenmesi Hakkında Kanun](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5651.pdf) — Log tutma yükümlülükleri ve zaman damgası (Timestamp) gereksinimleri.
- [ISO/IEC 27001:2022 - Ek A.8.15 (Loglama)](https://www.iso.org/standard/27001) — Logların kurcalanmaya karşı korunması (Non-repudiation / İnkâr edilemezlik) standardı.

## Key Findings / Temel Bulgular

1. **SQLi Sadece Teknik Değil, Yasal Bir İhlaldir:** KVKK emsal kararlarında (Örn: Veri tabanının SQL Injection ile sızdırılması), Kurul cezayı "sistemin hacklenmesine" değil, "OWASP standartlarına uygun Prepared Statements (Parametreli Sorgular) gibi bilinen güvenlik önlemlerinin alınmamış olmasına" (Madde 12 ihlali) kesmektedir. `/secure` rotamız kurumu doğrudan bu cezadan kurtarır.
2. **Unutulma Hakkı (Madde 7) ve Soft-Delete Yanılgısı:** Veritabanında sadece bir "is_deleted = 1" (soft delete) bayrağı bırakmak yasal olarak "Veri Yok Etme" sayılmamaktadır. Kusursuz Kasa projesinde uyguladığımız `DELETE FROM` (Hard Delete) yöntemi yasal olarak en güvenli yöntemdir.
3. **Loglar İspat Yükünün Kalbidir:** Bir kullanıcı "Verilerimi silmediler" diye kuruma şikayette bulunduğunda, şirketin elindeki tek savunma mekanizması bizim `audit.log` dosyamızdaki gibi değiştirilemez, zaman damgalı sistem kayıtlarıdır.

## Dead Ends / Çıkmaz Sokaklar

- **Logların Veritabanı İçinde Saklanması Yanılgısı:** Hukuki araştırmalarım sonucunda, sistem loglarının (audit.log) uygulamanın kendi veritabanında (SQLite) tutulmasının adli bilişim (Forensics) açısından zayıf kabul edildiğini gördüm.
  - *Sebep:* Eğer saldırgan veritabanını ele geçirirse, kendi izlerini (logları) da silebilir. Bu yüzden projede `Docker Volumes` kullanarak `audit.log` dosyasını konteynerin dışına, güvenli (izole) bir ortama çıkardık.

## Questions Remaining / Kalan Sorular

- [ ] Türkiye'deki 5651 Sayılı Kanun gereği, projemizdeki `audit.log` dosyasının TUBİTAK Zaman Damgası ile kriptografik olarak imzalanması sistematiği nasıl entegre edilebilir?
- [x] KVKK kapsamında veri taşınabilirliği (Madde 11) için JSON formatı yasal olarak yeterli mi? *(Cevap: Evet, yasa "yaygın olarak kullanılan, makinece okunabilir" format şartı koşar ve JSON günümüzün global standardıdır).*

## 50-Step Breakdown / 50 Adımlık Çözümleme (Özet: Yasal Bir Soruşturmada Sistemin Davranışı)

1. Adım: Kullanıcı KVKK Kurumu'na "Kusursuz Kasa verilerimi silmedi" şeklinde şikayette bulunur.
2. Adım: Kurul, veri sorumlusundan (sistem yöneticisinden) yasal savunma talep eder.
3. Adım: Sistem yöneticisi veritabanını (SQLite) sunar -> Kullanıcının verisi yoktur. (Yetersiz kanıt).
4. Adım: Sistem yöneticisi harici `audit.log` dosyasını sunar.
5. Adım: Adli bilişim uzmanları log dosyasındaki `2026-05-26 12:35:45 - KVKK MADDE 7: 'Ahmet' talebiyle veriler silindi` kaydını inceler.
6. Adım: Sistemin teknik olarak bu işlemi yerine getirdiği kanıtlanır, şirket cezadan kurtulur.
