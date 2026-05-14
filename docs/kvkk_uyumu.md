# KVKK ve Veri Mahremiyeti Uyumluluğu

Bu projede, güvenli yazılım geliştirmenin sadece teknik bir süreç olmadığı, aynı zamanda yasal mevzuata (KVKK) uyum gerektirdiği simüle edilmiştir.

## ⚖️ Hukuki Karşılaştırma
- **Kusurlu Rota:** Kullanıcı verileri, herhangi bir aydınlatma yükümlülüğü yerine getirilmeden ve açık rıza alınmadan toplanmaktadır. Bu durum KVKK Madde 5 ve Madde 10'a aykırılık teşkil eder.
- **Kusursuz Rota:** Veri toplama aşamasında kullanıcıya bir "Aydınlatma Metni" sunulmakta ve "Açık Rıza" (Opt-in) mekanizması ile veri işleme süreci hukuki bir dayanağa oturtulmaktadır.

## Uygulanan Mekanizma
Form üzerinden gelen `kvkk_consent` verisi sunucu tarafında doğrulanmadan veritabanına kayıt işlemi gerçekleştirilmemektedir.

## 🗑️ KVKK Madde 7: Unutulma Hakkı (Right to be Forgotten)
Kusursuz rota, kullanıcıların daha önce rıza göstererek işlenmesine izin verdikleri verileri **geri çekme** ve **kalıcı olarak sildirme** hakkını teknik olarak destekler. 

- Kullanıcı, `/secure/forget` uç noktası üzerinden yazar adını beyan ederek sistemdeki tüm kayıtlarını silebilir.
- Veritabanı işlemi, SQL Injection saldırılarını engellemek amacıyla `DELETE FROM notes WHERE author = ?` şeklinde *Prepared Statements* kullanılarak güvenli bir biçimde gerçekleştirilir.
