import requests
from tabulate import tabulate

def check_status(subdomains_file):
    # خواندن ساب دامین‌ها از فایل
    with open(subdomains_file, 'r') as file:
        subdomains = file.readlines()

    # حذف فضای خالی از ابتدا و انتهای هر خط
    subdomains = [subdomain.strip() for subdomain in subdomains]

    # لیست برای ذخیره نتایج
    results = []

    # چک کردن وضعیت هر ساب دامین
    for subdomain in subdomains:
        url = f'http://{subdomain}'
        try:
            response = requests.get(url, timeout=5)
            status_code = response.status_code
        except requests.exceptions.RequestException:
            status_code = 'Failed'

        # اضافه کردن نتیجه به لیست
        results.append([subdomain, status_code])

    # نمایش نتایج به صورت جدول
    print(tabulate(results, headers=["Subdomain", "Status Code"], tablefmt="grid"))

if __name__ == "__main__":
    # نام فایل ساب دامین‌ها را وارد کنید
    subdomains_file = 'subdomains.txt'
    check_status(subdomains_file)