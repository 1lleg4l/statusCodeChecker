import requests
import sys

def check_status(subdomains_file):
    try:
        # باز کردن فایل ورودی
        with open(subdomains_file, 'r') as file:
            subdomains = file.readlines()

        # بررسی وضعیت هر ساب‌دامین
        for subdomain in subdomains:
            subdomain = subdomain.strip()  # حذف فاصله‌ها و کاراکترهای اضافی
            url = f"http://{subdomain}"  # آدرس URL ساب‌دامین
            try:
                response = requests.get(url)
                print(f"{subdomain} - Status Code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"{subdomain} - Error: {str(e)}")
    except FileNotFoundError:
        print(f"File '{subdomains_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # گرفتن نام فایل از ورودی
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <subdomains_file>")
        sys.exit(1)

    subdomains_file = sys.argv[1]  # گرفتن نام فایل از ورودی
    check_status(subdomains_file)
