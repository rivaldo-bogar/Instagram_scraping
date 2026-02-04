import time
import random
import json
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

COOKIE_FILE = "cookies.json"

def load_cookies_selenium(driver):
    if not os.path.exists(COOKIE_FILE): return False
    driver.get("https://www.instagram.com")
    time.sleep(3)
    with open(COOKIE_FILE, 'r') as f:
        cookies = json.load(f)
    for cookie in cookies:
        if 'sameSite' in cookie: del cookie['sameSite']
        try: driver.add_cookie(cookie)
        except: continue
    driver.refresh()
    time.sleep(5)
    return True

def scroll_paling_barbar(driver, type_label):
    print(f"🚀 Memulai Brute-Force Scroll untuk {type_label}...")
    
    usernames = set()
    no_new_data_count = 0
    
    # 1. Tekan TAB beberapa kali untuk memindahkan fokus ke dalam pop-up
    # Ini trik paling ampuh jika elemen tidak ditemukan
    for _ in range(5):
        webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
        time.sleep(0.2)

    while no_new_data_count < 10: # Coba 10x scroll jika data tidak nambah
        # AMBIL DATA: Cari semua elemen yang mengandung teks username
        # Kita gunakan XPATH yang sangat luas agar tidak luput
        current_len = len(usernames)
        found_elements = driver.find_elements(By.XPATH, "//div[@role='dialog']//span//a[@role='link']//span")
        
        for el in found_elements:
            name = el.text.strip()
            if name and len(name) > 1:
                usernames.add(name)

        # 2. EKSEKUSI SCROLL: Kirim perintah PAGE_DOWN berkali-kali
        for _ in range(3):
            webdriver.ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(0.5)

        print(f"   > Progress: {len(usernames)} {type_label} didapatkan...")

        if len(usernames) == current_len:
            no_new_data_count += 1
            # Jika macet, coba tekan END sekali
            webdriver.ActionChains(driver).send_keys(Keys.END).perform()
        else:
            no_new_data_count = 0
        
        time.sleep(random.uniform(1.5, 3.0))

    return list(usernames)

def main():
    target = input("Masukkan Username Target: ").strip().replace("@", "")
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    try:
        if not load_cookies_selenium(driver): return
        driver.get(f"https://www.instagram.com/{target}/")
        time.sleep(5)

        results = {}
        # Cari link followers/following dengan XPATH berdasarkan teks (mendukung ID/EN)
        for mode in ['follower', 'following']:
            try:
                print(f"\n--- Mencoba klik menu {mode} ---")
                # Cari elemen <a> yang href-nya mengandung kata follower/following
                btn = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, f"//a[contains(@href, '/{mode}')]"))
                )
                driver.execute_script("arguments[0].click();", btn) # Klik via JS agar lebih stabil
                time.sleep(5)
                
                label = "Followers" if "follower" in mode else "Following"
                results[label] = scroll_paling_barbar(driver, label)
                
                # Tutup pop-up
                webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                time.sleep(2)
            except Exception as e:
                print(f"⚠️ Melewati {mode}: {e}")

        # SIMPAN KE EXCEL
        df = pd.DataFrame({
            'Followers': pd.Series(results.get('Followers', [])),
            'Following': pd.Series(results.get('Following', []))
        })
        
        df.to_excel(f"HASIL_MAKSIMAL_{target}.xlsx", index=False)
        print(f"\n🏆 SELESAI! Cek file: HASIL_MAKSIMAL_{target}.xlsx")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()