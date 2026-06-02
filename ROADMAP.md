# ROADMAP — OWASP Secure Vault & KVKK Compliance Portal[cite: 3]
# ROADMAP — Kusursuz Kasa ve Hukuki Uyum Portalı[cite: 3]

> Course / Ders: Secure Web Development (BGT208) · Istinye University[cite: 3]
> Instructor / Danışman: Keyvan Arasteh[cite: 3]

---

## Phase 0 / Faz 0: Understand Before You Build / Yazmadan Önce Anla[cite: 3]

Before writing a single line of code, I answered these questions:[cite: 3]
Tek satır kod yazmadan önce şu soruları yanıtladım:[cite: 3]

- **What is the project? / Proje nedir?**[cite: 3] A dual-route web application demonstrating both security vulnerabilities (SQLi, XSS, CSRF) and their industry-standard fixes alongside legal compliance mechanisms (KVKK/GDPR, ISO 27001).
- **How does it work? / Nasıl çalışır?**[cite: 3] Users interact with a vulnerable route to exploit standard web vulnerabilities or use a secure route protected by Prepared Statements, input escaping, and CSRF tokens.
- **What are the inputs/outputs? / Girdiler/çıktılar neler?**[cite: 3] User text inputs (notes, author names) and consent checkboxes outputting to a SQLite database, JSON data portability exports, and structured ISO 27001 audit logs.
- **What tools will I use and why? / Hangi araçları kullanacağım ve neden?**[cite: 3] Python (Flask) for backend logic, Jinja2 for templating, SQLite for lightweight data management, and Docker for containerized deployment.

---

## Phase 1 / Faz 1: Research & Investigation / Araştırma ve Keşif[cite: 3]

> Folder / Klasör: `docs/research/`[cite: 3]

| Topic / Konu | Status / Durum | Notes / Notlar |
|--------------|----------------|----------------|
| OWASP Vulnerabilities (SQLi, XSS) | ✅ Completed | Analyzed mitigation strategies like parameterization and sanitization (`sqli_anatomisi.md`, `xss_anatomisi.md`). |
| KVKK/GDPR Regulations | ✅ Completed | Researched Art. 7 (Right to be Forgotten) and Art. 11 (Data Portability) mechanisms (`kvkk_uyumu.md`). |
| ISO 27001 Logging Standards | ✅ Completed | Investigated non-repudiation and centralized logging requirements for digital forensics (`iso27001_loglama.md`). |

---

## Phase 2 / Faz 2: Environment Setup / Ortam Kurulumu[cite: 3]

- [x] Isolated lab environment (Docker / VM) / İzole lab ortamı[cite: 3]
- [x] Tools installed and verified / Araçlar kuruldu ve test edildi[cite: 3]
- [x] `.env.example` created / oluşturuldu[cite: 3]

---

## Phase 3 / Faz 3: Implementation / Uygulama[cite: 3]

### Module / Modül: Core Architecture & Vulnerabilities[cite: 3]

1. Step 1 / Adım 1 — Developed the base Flask architecture and SQLite database initialization schema.[cite: 3]
2. Step 2 / Adım 2 — Created the "Vulnerable Route" simulating SQL Injection and Stored XSS.[cite: 3]
3. Step 3 / Adım 3 — Built the "Secure Route" implementing Prepared Statements, CSRF tokens, and Jinja2 auto-escaping.[cite: 3]

### Module / Modül: Legal Compliance & Forensics (KVKK & ISO 27001)[cite: 3]

1. Step 1 / Adım 1 — Integrated a strict KVKK consent gateway for data entry.[cite: 3]
2. Step 2 / Adım 2 — Implemented the "Right to be Forgotten" module for permanent data deletion (KVKK Art 7).[cite: 3]
3. Step 3 / Adım 3 — Developed a Data Portability feature allowing users to export their structured data in JSON format (KVKK Art 11).[cite: 3]
4. Step 4 / Adım 4 — Configured system-wide ISO 27001 compliant audit logging (`audit.log`) for all critical operations.[cite: 3]

---

## Phase 4 / Faz 4: Testing & Reporting / Test ve Raporlama[cite: 3]

- [x] Ran tests against target/sample / Hedef/örnek üzerinde testler çalıştırıldı[cite: 3] (XSS payloads, SQLi bypass attempts)
- [x] Documented all findings with evidence / Tüm bulgular kanıtlarıyla belgelendi[cite: 3]
- [x] Wrote final report (Markdown) / Final raporu yazıldı[cite: 3]

---

## Phase 5 / Faz 5: Delivery / Teslim[cite: 3]

- [x] GitHub repository is clean and organized / Repo temiz ve düzenli[cite: 3]
- [x] README.md complete / eksiksiz[cite: 3]
- [x] Docker verified (`docker-compose up`) / doğrulandı[cite: 3]
- [x] Instructor invited as collaborator / Danışman collaborator olarak eklendi → **keyvanarasteh**[cite: 3]

---

## What I Learned / Öğrendiklerim[cite: 3]

Integrating legal frameworks (like KVKK and GDPR) directly into the technical architecture of a software project was a profound experience. I learned that true web security isn't just about preventing unauthorized technical access via SQLi or XSS; it also requires building transparent, auditable mechanisms (like Data Portability and ISO 27001 logging) that protect the user's legal rights and privacy. Furthermore, standardizing the deployment via Docker and maintaining code quality with CI/CD solidified my understanding of professional DevSecOps lifecycles.[cite: 3]
