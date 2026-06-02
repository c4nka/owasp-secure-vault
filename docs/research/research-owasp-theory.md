# Research Notes / Araştırma Notları

> Module / Konu: OWASP Top 10 Zafiyetlerinin Çekirdek (Kernel/Engine) Seviyesinde İncelenmesi
> Date / Tarih: 2026-06-02

---

## What I'm Investigating / Araştırdığım Konu

Bu araştırmanın amacı, web güvenlik zafiyetlerini (özellikle SQL Injection ve XSS) yüzeysel "payload" seviyesinden çıkarıp, arka planda çalışan dil motorları ve derleyiciler (Parsers & Interpreters) seviyesinde anlamaktır. Parametreli sorguların veritabanı motoru tarafından nasıl işlendiğini ve tarayıcıların XSS saldırılarını engellemek için Content Security Policy'yi (CSP) ağ katmanında nasıl uyguladığını araştırıyorum.

## Resources Found / Bulunan Kaynaklar

- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) — Birincil savunma olan Prepared Statements (Parametreli Sorgular) mimarisinin standartları.
- [Database Abstract Syntax Tree (AST) Architecture](https://en.wikipedia.org/wiki/Abstract_syntax_tree) — SQL motorlarının gelen sorguyu nasıl parse edip (ayrıştırıp) mantıksal ağaçlara böldüğünün teorisi.
- [MDN Web Docs: Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) — Modern tarayıcıların inline (satıriçi) script yürütmeyi HTTP başlıkları (Headers) seviyesinde nasıl reddettiği.

## Key Findings / Temel Bulgular

1. **SQLi ve AST İlişkisi:** Güvenli olmayan (String Concatenation) yönteminde, saldırganın girdiği `DROP TABLE` komutu SQL ayrıştırıcısı (parser) tarafından doğrudan "Çalıştırılabilir Kod Düğümü" (Executable Node) olarak AST'ye (Abstract Syntax Tree) eklenir. 
2. **Prepared Statements'ın Matematiği:** Parametreli sorgular (`?` veya `%s`) kullanıldığında ise, sorgu şablonu (Query Template) önceden derlenir. Kullanıcıdan gelen veri bu şablona dahil edildiğinde, SQL motoru bu veriyi asla yeni bir komut olarak parse etmez; onu yalnızca önceden derlenmiş ağacın içindeki bir "Veri Değişkeni" (Literal Value) olarak kabul eder. Bu matematiksel bir izolasyondur.
3. **XSS ve Derinlemesine Savunma:** HTML Entity Encoding (`escape()`) kullanmak veriyi zararsız metne dönüştürse de, sistem seviyesinde tam bir koruma için CSP (Content Security Policy) şarttır. CSP `default-src 'self'` kuralı uygulandığında, tarayıcı sayfaya dışarıdan sızmış hiçbir JavaScript dosyasını veya `<script>` etiketini çalıştırmaz.

## Dead Ends / Çıkmaz Sokaklar

- **Kara Liste (Blacklisting) ile SQLi Koruması:** `SELECT`, `DROP`, `OR` gibi kelimeleri filtreleyen bir fonksiyon yazılması teorik olarak incelendi.
  - *Sonuç:* Başarısız. Saldırganlar `SeLeCt` yazarak, hex/URL encoding kullanarak veya farklı karakter setleri (Unicode) ile bu filtreleri kolayca aşabilir. Sadece beyaz liste (Whitelisting) veya parametrizasyon kesin çözümdür.

## Questions Remaining / Kalan Sorular

- [x] Zaman tabanlı kör SQL Injection (Time-based Blind SQLi) parametreli sorguları aşabilir mi? *(Cevap: Hayır, AST izole edildiği için `WAITFOR DELAY` komutu da sadece bir metin olarak algılanır).*
- [ ] Projeye HTTP katmanında (Flask üzerinden) katı bir CSP (Content Security Policy) header'ı nasıl entegre edilebilir?

## 50-Step Breakdown / 50 Adımlık Çözümleme (Özet: SQL Parametrizasyon Süreci)

1. Adım: Uygulama, SQL motoruna (Örn: SQLite) içinde `?` bulunan bir sorgu şablonu gönderir.
2. Adım: SQL motoru bu şablonu "Parse" eder ve bir AST (Sözdizim Ağacı) oluşturur.
3. Adım: Motor, şablonu çalışmaya hazır (derlenmiş) hale getirir ve beklemeye alır.
4. Adım: Uygulama, kullanıcıdan gelen ham veriyi (zararlı kod içerse bile) SQL motoruna parametre olarak gönderir.
5. Adım: SQL motoru, derlenmiş şablonu yeniden "Parse" ETMEZ. Veriyi sadece ilgili "Variable/Value" boşluğuna bir string olarak yerleştirir ve sorguyu çalıştırır.
