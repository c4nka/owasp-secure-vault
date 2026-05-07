# SQL Injection (SQLi) Anatomisi ve Savunma

Bu projede SQL Injection zafiyetinin nasıl oluştuğu ve nasıl engellendiği uygulamalı olarak gösterilmiştir.

## 💥 Kusurlu Yaklaşım (Zafiyetin Nedeni)
`vulnerable.py` içerisinde kullanıcıdan alınan girdi, hiçbir filtrelemeden geçirilmeden `f-string` kullanılarak doğrudan SQL sorgusuna yerleştirilir:
```python
query = f"INSERT INTO notes (content, author) VALUES ('{content}', '{author}')"
```

Saldırgan forma ' OR 1=1 -- gibi bir payload girdiğinde, veritabanı bunu düz metin değil, çalıştırılabilir bir komut olarak algılar ve sorgunun mantığını bozar.
