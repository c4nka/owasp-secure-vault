# ISO 27001 Uyumlu Denetim İzi (Audit Logging)

Bu projede, güvenli yazılım mimarisinin en kritik yapı taşlarından biri olan izlenebilirlik ve denetlenebilirlik mekanizmaları kurgulanmıştır.

## 🛡️ ISO/IEC 27001 Referansı
Projede uygulanan loglama altyapısı, **ISO 27001 Ek A.12.4 (Günlük Kaydetme ve İzleme)** kontrolleriyle tam uyumludur:
- **Değiştirilemezlik:** Log kayıtları, uygulama veritabanından bağımsız olarak sunucu seviyesinde `audit.log` dosyasında tutulur.
- **Kritik Olay Takibi:** Sadece rutin işlemler değil; yetkisiz erişim denemeleri (CSRF ihlalleri) ve KVKK uyum süreçleri `WARNING` ve `ERROR` seviyelerinde kayıt altına alınır.

## ⚖️ Hukuki ve Adli Bilişim Boyutu
Olası bir veri sızıntısı veya yasal uyuşmazlık anında, silme (Madde 7) veya taşıma (Madde 11) taleplerinin ne zaman ve kimin tarafından gerçekleştirildiği adli makamlara doğrulanabilir zaman damgalı (Timestamp) bu denetim izleriyle ispat edilir.
