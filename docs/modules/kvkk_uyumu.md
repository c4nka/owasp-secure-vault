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

## 📦 KVKK Madde 11 ve GDPR Madde 20: Veri Taşınabilirliği (Data Portability)
Kusursuz rota, modern veri mahremiyeti yasalarının en kritik taleplerinden biri olan veri taşınabilirliğini teknik olarak yerine getirir.

- `/secure/download` uç noktası, ilgili veri sahibinin talebi üzerine veritabanında sadece o kişiye ait verileri filtreler.
- Elde edilen veriler, uluslararası standartlara uygun, makinece okunabilir yapılandırılmış **JSON** formatına dönüştürülerek kullanıcıya şifreli bir oturum tüneli üzerinden indirilir.
- Sorgu aşamasında *Prepared Statements* kullanılarak veri sızıntısı veya yetkisiz veri çekme (IDOR/SQLi) riskleri tamamen engellenmiştir.
