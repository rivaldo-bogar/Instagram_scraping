import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def generate_instagram_cookies():
    # Setup Chrome options
    chrome_options = Options()
    # Menghilangkan deteksi bot agar login lebih aman
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    # Inisialisasi Driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    print("Membuka Instagram... Silakan login secara manual di jendela browser yang muncul.")
    driver.get("https://www.instagram.com/accounts/login/")
    
    # Beri waktu pengguna untuk login dan melewati 2FA
    print("MENUNGGU LOGIN: Silakan masukkan username, password, dan kode 2FA Anda.")
    print("Jika sudah masuk ke Beranda/Home Instagram, kembali ke sini dan tekan ENTER.")
    
    input("Tekan ENTER di sini jika Anda sudah berhasil masuk ke Beranda Instagram...")

    # Ambil cookies setelah login berhasil
    cookies = driver.get_cookies()
    
    # Simpan ke file JSON
    with open("cookies.json", "w") as f:
        json.dump(cookies, f, indent=4)
    
    print("\n✅ BERHASIL! File 'cookies.json' telah dibuat.")
    print("Sekarang Anda bisa menjalankan kode scraper utama.")
    
    driver.quit()

if __name__ == "__main__":
    generate_instagram_cookies()