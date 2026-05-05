<div align="center">
  <img src="https://images.seeklogo.com/logo-png/61/1/istinye-universitesi-logo-png_seeklogo-610039.png" width="300" alt="İstinye Üniversitesi Logosu">
</div>

# OWASP Karşılaştırmalı Web Portalı (Secure vs. Vulnerable Vault)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Framework-Flask-black?style=flat-square&logo=flask)
![Security](https://img.shields.io/badge/OWASP-Top%2010%20Focus-red?style=flat-square)

## Proje Bilgileri
* **Kurum:** İstinye Üniversitesi
* **Ders:** Bilişim Güvenliği Teknolojisi - Güvenli Web Yazılımı Geliştirme
* **Danışman / Eğitmen:** [Danışman Hocanın Adı Soyadı]
* **Geliştirici:** Raşit Çankaya

## İçindekiler
- [Proje Hakkında](#proje-hakkında)
- [Mimari Yaklaşım](#mimari-yaklaşım)
- [Uygulanan Saldırı ve Savunma Senaryoları](#uygulanan-saldırı-ve-savunma-senaryoları)
- [Kurulum](#kurulum)

## Proje Hakkında
Bu proje, web uygulamalarındaki temel güvenlik zafiyetlerini (OWASP Top 10) uygulamalı olarak göstermek ve aynı zafiyetlerin modern güvenli yazılım geliştirme prensipleriyle nasıl giderildiğini kanıtlamak amacıyla geliştirilmiştir.

Uygulama iki farklı rotadan (route) oluşur:
1. **Kusurlu Rota (Vulnerable):** Siber saldırılara (SQLi, XSS) tamamen açık, zayıf kodlanmış bölüm.
2. **Kusursuz Rota (Secure):** Girdi temizleme (sanitization), prepared statements ve CSRF token'ları kullanılarak sıkılaştırılmış güvenli bölüm.

*(Not: Proje aktif geliştirme aşamasındadır.)*
