# SQL Injection (SQLi) Anatomisi ve Savunma

Bu projede SQL Injection zafiyetinin nasıl oluştuğu ve nasıl engellendiği uygulamalı olarak gösterilmiştir.

## 💥 Kusurlu Yaklaşım (Zafiyetin Nedeni)
`vulnerable.py` içerisinde kullanıcıdan alınan girdi, hiçbir filtrelemeden geçirilmeden `f-string` kullanılarak doğrudan SQL sorgusuna yerleştirilir:
```python
query = f"INSERT INTO notes (content, author) VALUES ('{content}', '{author}')"
```

Saldırgan forma ' OR 1=1 -- gibi bir payload girdiğinde, veritabanı bunu düz metin değil, çalıştırılabilir bir komut olarak algılar ve sorgunun mantığını bozar.

🛡️ Kusursuz Yaklaşım (Savunma)

secure.py içerisinde bu zafiyet, endüstri standardı olan Prepared Statements (Parametreli Sorgular) kullanılarak tamamen kapatılmıştır:

```python
query = "INSERT INTO notes (content, author) VALUES (?, ?)"
conn.execute(query, (clean_content, clean_author))
```

Burada soru işaretleri (?) yer tutucu olarak işlev görür. Veritabanı, dışarıdan gelen veriyi yapısal bir komut olarak değil, sadece "değer" olarak işler.

```markdown
# Cross-Site Scripting (XSS) Anatomisi ve Savunma

Web uygulamalarında sıkça karşılaşılan XSS (Stored XSS) zafiyeti, projenin kusurlu rotasında simüle edilmiştir.

## 💥 Kusurlu Yaklaşım (Zafiyetin Nedeni)
Kullanıcıların notlarını ekrana basarken Jinja2 template motorundaki `| safe` filtresi bilerek kullanılmıştır:
```html
{{ note.content | safe }}
```

Bu filtre, veritabanına kaydedilen HTML ve Javascript etiketlerinin (<script>alert(1);</script>) tarayıcı tarafından doğrudan çalıştırılmasına neden olur.

🛡️ Kusursuz Yaklaşım (Savunma)

secure.py rotasında dışarıdan alınan tüm girdiler işlenmeden önce Input Escape (Sanitization) işleminden geçirilir:

```python
from markupsafe import escape
clean_content = escape(content)
```

Ayrıca güvenli şablonda (secure.html), Jinja2'nin varsayılan davranışı olan otomatik kaçış (auto-escaping) özelliği kullanılarak, zararlı kod parçacıklarının düz metne (string) dönüştürülmesi sağlanır.

Tüm dosyaları kaydettikten sonra, zaman yatırımı kuralına uygun olması için bu dosyaları da bilgisayarında birkaç gün bekletmeni tavsiye ederim (Örneğin Docker commitinden 1 gün sonra). Atacağın commit komutları şu şekilde olmalıdır:

```bash
git add .
git commit -m "docs: added CI/CD workflow, MIT license, and comprehensive vulnerability anatomy documentation"
git push origin main,
```
