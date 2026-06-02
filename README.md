<div align="center">
  <a href="https://istinye.edu.tr">
    <img src="https://images.seeklogo.com/logo-png/61/1/istinye-universitesi-logo-png_seeklogo-610039.png" width="300" alt="İstinye Üniversitesi Logosu"/>
  </a>

  # OWASP Secure Vault & KVKK Compliance Portal

  ![GitHub](https://img.shields.io/badge/GitHub-Private-red?style=flat-square&logo=github)
  ![Language](https://img.shields.io/badge/Language-Python-blue?style=flat-square)
  ![Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)
  ![Course](https://img.shields.io/badge/Course-BGT208-purple?style=flat-square)
  ![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
</div>

---

## 🎓 Instructor / Danışman

| | |
|---|---|
| **Name / Ad** | Keyvan Arasteh |
| **GitHub** | [@keyvanarasteh](https://github.com/keyvanarasteh) |
| **Email** | [keyvan.arasteh@istinye.edu.tr](mailto:keyvan.arasteh@istinye.edu.tr) |
| **LinkedIn** | [keyvanarasteh](https://www.linkedin.com/in/keyvanarasteh/) |
| **Website** | [qline.tech](https://qline.tech) |

---

## 👤 Student / Öğrenci

| | |
|---|---|
| **Name / Ad Soyad** | Raşit Çankaya |
| **Student ID / Öğrenci No** | `2420191006` |

---

## 📚 Course Information / Ders Bilgileri

| | |
|---|---|
| **Course Name / Ders Adı** | Secure Web Development / Güvenli Web Yazılımı Geliştirme |
| **Course Code / Ders Kodu** | BGT208 |
| **Credits / Kredi** | 3 ECTS |
| **Semester / Dönem** | 2025-2026 Spring / 2025-2026 Bahar |
| **Institution / Üniversite** | [Istinye University](https://istinye.edu.tr) |

---

## 📋 Project Overview / Proje Özeti

This project is a Flask-based web application demonstrating the critical differences between vulnerable and secure coding practices. It goes beyond technical mitigation of OWASP Top 10 vulnerabilities (SQLi, XSS, CSRF) by implementing strict legal compliance features. The architecture includes automated data portability, right-to-be-forgotten mechanisms under KVKK/GDPR, and ISO 27001 compliant audit logging.

Bu proje, zafiyetli ve güvenli kodlama pratikleri arasındaki farkları uygulamalı olarak gösteren Flask tabanlı bir web platformudur. OWASP Top 10 zafiyetlerinin (SQLi, XSS, CSRF) teknik savunmalarının ötesine geçerek hukuki uyumluluk modüllerini barındırır. Mimari, KVKK/GDPR kapsamında unutulma hakkı, veri taşınabilirliği ve ISO 27001 uyumlu denetim izi (audit logging) sistemlerini içermektedir.

---

## 🗂 Repository Structure / Repo Yapısı

```text
.
├── .github/workflows/    # CI/CD Pipelines (Flake8)
├── docs/                 # Vulnerability anatomies & legal compliance documentation
├── src/                  # Core application source code
├── requirements.txt      # Python dependencies
├── Dockerfile            # Container build instructions
├── docker-compose.yml    # Container orchestration & volume mapping
├── audit.log             # ISO 27001 compliance logs
├── LICENSE               # MIT License
├── README.md
└── ROADMAP.md
```
## 🚀 Getting Started / Kurulum

```bash
git clone [https://github.com/rasitcankaya/](https://github.com/rasitcankaya/)[your-repo]
cd [your-repo]

# Start the application with Docker / Uygulamayı Docker ile başlatın
docker-compose up --build -d

# Uygulama http://localhost:5000 adresinde çalışacaktır.
```

## 📊 Deliverables / Teslimler

| Item | Status |
|------|--------|
| Implementation of Vulnerable vs. Secure Routes (SQLi, XSS, CSRF) | ✅ |
| KVKK/GDPR Compliance (Consent, Right to be Forgotten, Data Portability) | ✅ |
| ISO 27001 Compliant Audit Logging Mechanism | ✅ |
| Dockerization and CI/CD Pipeline (GitHub Actions) Integration | ✅ |
| Comprehensive Markdown Documentation | ✅ |

---

## 📚 Documentation / Belgeleme

All vulnerability and compliance docs → [`docs/`](./docs/)
- `sqli_anatomisi.md`
- `xss_anatomisi.md`
- `kvkk_uyumu.md`
- `iso27001_loglama.md`

---

## 🔗 References / Kaynaklar

- [OWASP Top 10 (2021)](https://owasp.org/Top10/)
- [Kişisel Verilerin Korunması Kanunu (KVKK)](https://www.kvkk.gov.tr/)
- [ISO/IEC 27001 Information Security Management](https://www.iso.org/isoiec-27001-information-security.html)
