# KVKK ve Veri Mahremiyeti Uyumluluğu

Bu projede, güvenli yazılım geliştirmenin sadece teknik bir süreç olmadığı, aynı zamanda yasal mevzuata (KVKK) uyum gerektirdiği simüle edilmiştir.

## ⚖️ Hukuki Karşılaştırma
- **Kusurlu Rota:** Kullanıcı verileri, herhangi bir aydınlatma yükümlülüğü yerine getirilmeden ve açık rıza alınmadan toplanmaktadır. Bu durum KVKK Madde 5 ve Madde 10'a aykırılık teşkil eder.
- **Kusursuz Rota:** Veri toplama aşamasında kullanıcıya bir "Aydınlatma Metni" sunulmakta ve "Açık Rıza" (Opt-in) mekanizması ile veri işleme süreci hukuki bir dayanağa oturtulmaktadır.

## Uygulanan Mekanizma
Form üzerinden gelen `kvkk_consent` verisi sunucu tarafında doğrulanmadan veritabanına kayıt işlemi gerçekleştirilmemektedir.
