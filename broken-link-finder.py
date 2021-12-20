from bs4 import BeautifulSoup, SoupStrainer
import requests

# تعریف یوآرال برای گرفتن ادرس از کاربر
url = input("linke khod ra vared conid: ")

# ذخیره یوآرال
page = requests.get(url)

# گرفتن کد ریسپانس 
response_code = str(page.status_code)

# نشان دادن یوآر ال های داخلی
data = page.text

# استفاده از بیوتیفول سوپ
soup = BeautifulSoup(data)

# نشان دادن استتوس لینک های داخلی
for link in soup.find_all('a'):
    print(f"Url: {link.get('href')} " + f"| Status Code: {response_code}")