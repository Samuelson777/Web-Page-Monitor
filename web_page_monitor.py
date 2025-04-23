import requests
import time
import hashlib

def get_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

def hash_content(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def monitor_page(url, check_interval):
    previous_hash = None

    while True:
        current_content = get_page_content(url)
        if current_content is None:
            time.sleep(check_interval)
            continue

        current_hash = hash_content(current_content)

        if previous_hash and current_hash != previous_hash:
            print(f"Change detected on {url}!")

        previous_hash = current_hash
        time.sleep(check_interval)

if __name__ == "__main__":
    target_url = input("Enter the URL to monitor: ")
    interval = int(input("Enter the check interval in seconds: "))
    monitor_page(target_url, interval)