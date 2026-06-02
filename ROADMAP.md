# ROADMAP — OWASP Secure Vault & KVKK Compliance Portal
# ROADMAP — Kusursuz Kasa ve Hukuki Uyum Portalı

> Course / Ders: Secure Web Development (BGT208) · Istinye University
> Instructor / Danışman: Keyvan Arasteh[

---

## Phase 0 / Faz 0: Understand Before You Build / Yazmadan Önce Anla

Before writing a single line of code, I answered these questions:
Tek satır kod yazmadan önce şu soruları yanıtladım:

- **What is the project? / Proje nedir?** A dual-route web application demonstrating both security vulnerabilities (SQLi, XSS, CSRF) and their industry-standard fixes alongside legal compliance mechanisms (KVKK/GDPR, ISO 27001).
- **How does it work? / Nasıl çalışır?** Users interact with a vulnerable route to exploit standard web vulnerabilities or use a secure route protected by Prepared Statements, input escaping, and CSRF tokens.
- **What are the inputs/outputs? / Girdiler/çıktılar neler?** User text inputs (notes, author names) and consent checkboxes outputting to a SQLite database, JSON data portability exports, and structured ISO 27001 audit logs.
- **What tools will I use and why? / Hangi araçları kullanacağım ve neden?** Python (Flask) for backend logic, Jinja2 for templating, SQLite for lightweight data management, and Docker for containerized deployment.

---

## Phase 1 / Faz 1: Research & Investigation / Araştırma ve Keşif

> Folder / Klasör: `docs/research/`

| Topic / Konu | Status / Durum | Notes / Notlar |
|--------------|----------------|----------------|
| OWASP Vulnerabilities (SQLi, XSS) | ✅ Completed | Analyzed mitigation strategies like parameterization and sanitization (`sqli_anatomisi.md`, `xss_anatomisi.md`). |
| KVKK/GDPR Regulations | ✅ Completed | Researched Art. 7 (Right to be Forgotten) and Art. 11 (Data Portability) mechanisms (`kvkk_uyumu.md`). |
| ISO 27001 Logging Standards | ✅ Completed | Investigated non-repudiation and centralized logging requirements for digital forensics (`iso27001_loglama.md`). |

---

## Phase 2 / Faz 2: Environment Setup / Ortam Kurulumu

- [x] Isolated lab environment (Docker / VM) / İzole lab ortamı
- [x] Tools installed and verified / Araçlar kuruldu ve test edildi
- [x] `.env.example` created / oluşturuldu

---

## Phase 3 / Faz 3: Implementation / Uygulama

### Module / Modül: Core Architecture & Vulnerabilities

1. Step 1 / Adım 1 — Developed the base Flask architecture and SQLite database initialization schema.
2. Step 2 / Adım 2 — Created the "Vulnerable Route" simulating SQL Injection and Stored XSS.
3. Step 3 / Adım 3 — Built the "Secure Route" implementing Prepared Statements, CSRF tokens, and Jinja2 auto-escaping.

### Module / Modül: Legal Compliance & Forensics (KVKK & ISO 27001)

1. Step 1 / Adım 1 — Integrated a strict KVKK consent gateway for data entry.
2. Step 2 / Adım 2 — Implemented the "Right to be Forgotten" module for permanent data deletion (KVKK Art 7).
3. Step 3 / Adım 3 — Developed a Data Portability feature allowing users to export their structured data in JSON format (KVKK Art 11).
4. Step 4 / Adım 4 — Configured system-wide ISO 27001 compliant audit logging (`audit.log`) for all critical operations.

---

## Phase 4 / Faz 4: Testing & Reporting / Test ve Raporlama

- [x] Ran tests against target/sample / Hedef/örnek üzerinde testler çalıştırıldı (XSS payloads, SQLi bypass attempts)
- [x] Documented all findings with evidence / Tüm bulgular kanıtlarıyla belgelendi
- [x] Wrote final report (Markdown) / Final raporu yazıldı

---

## Phase 5 / Faz 5: Delivery / Teslim

- [x] GitHub repository is clean and organized / Repo temiz ve düzenli
- [x] README.md complete / eksiksiz
- [x] Docker verified (`docker-compose up`) / doğrulandı
- [x] Instructor invited as collaborator / Danışman collaborator olarak eklendi → **keyvanarasteh**

---

## What I Learned / Öğrendiklerim

Integrating legal frameworks (like KVKK and GDPR) directly into the technical architecture of a software project was a profound experience. I learned that true web security isn't just about preventing unauthorized technical access via SQLi or XSS; it also requires building transparent, auditable mechanisms (like Data Portability and ISO 27001 logging) that protect the user's legal rights and privacy. Furthermore, standardizing the deployment via Docker and maintaining code quality with CI/CD solidified my understanding of professional DevSecOps lifecycles.
