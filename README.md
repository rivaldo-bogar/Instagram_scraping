# 📸 Automation WebDriver Project: Instagram Scraping

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)


Sistem ini mengambil otomatis followers dan following dari user lain di instagram,dengan catatan kalian sudah berteman, dan menggunakan metode login dengan cookie,jadi nanti cookie anda agar tersimpan ke cookie.json

## 🚀 Fitur Utama
* **Mengambil followers dan following secara otomatis.
* **Menyimpan followers dan following ke file xlxs.


## 🛠️ Prasyarat (Prerequisites)
Pastikan kamu sudah menginstal Python 3.8 ke atas di laptopmu.

## 📦 Instalasi
Ikuti langkah-langkah berikut untuk menjalankan project ini di lokal:

1. **Clone Repository**
   ```bash
   git clone [https://github.com/username/nama-repo.git](https://github.com/username/nama-repo.git)
   cd nama-repo
2. **Buat virtual environment**
   ```bash
   python -m venv
3. **Aktfikan venv (windows)**
   ```bash
   venv\Scripts\activate
   ```
   **Aktfikan venv (mac\linux)**
   ```bash
   source venv/bin/activate
   ```
4. **Install modul/library**
   ```bash
   pip install -r requirements.txt
   ```
5. **Jalankan file generate_cookie (masukan email/username dan pw IG) **
   ```bash
   python generate_cookie.py
   ```
6. **Jalankan ig_scraper.py**
   ```bash
   python ig_scraper.py
   
   
