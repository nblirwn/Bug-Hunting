import requests
import time
import random

def check_urls_for_keyword(input_file, output_file, keyword):
    try:
        with open(input_file, 'r') as file:
            urls = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{input_file}' tidak ditemukan.")
        return

    print(f"Memulai pengecekan pada {len(urls)} URL...")
    print("-" * 50)

    positive_urls = []
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    for url in urls:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            
            if keyword.lower() in response.text.lower():
                print(f"[+] Positive: {url}")
                positive_urls.append(url)
            else:
                print(f"[-] Negative  : {url}")
                
        except requests.exceptions.RequestException as e:
            print(f"[!] ERROR      : {url} (Alasan: {type(e).__name__})")

        time.sleep(random.uniform(0.5, 1))

    with open(output_file, 'w') as file:
        for p_url in positive_urls:
            file.write(p_url + "\n")

    print("-" * 50)
    print(f"Pengecekan selesai! Ditemukan {len(positive_urls)} PHP error.")

if __name__ == "__main__":
    check_urls_for_keyword("url.txt", "positive.txt", "a php error")
