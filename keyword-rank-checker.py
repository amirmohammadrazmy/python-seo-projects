import requests
import os

#گرفتن api از استک
api_key = "d79876d2ae3c32771c1d4f06dab9aaf6" 
query = input("enter your keyword here: ") 
target_domain = input("enter your domain here: ") 
google_domain = "google.com" 
country_code = "US" 
language = "fa" 
results = 50 
device = "mobile" 


#درست کردن پارامترهای api
params = {
  'access_key': api_key,
  'device': device,
  'gl': country_code,
  'hl': language,
  'auto_location': '1',
  'google_domain':google_domain,
  'query': query,
  'num': results
}

# صدا زدن api
api_result = requests.get('http://api.serpstack.com/search', params)
api_response = api_result.json()

#نشون دادن سایتها در کنسول
for number, result in enumerate(api_response['organic_results'], start=1):
    if target_domain in result['domain']:
      print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
      print("%s. %s - %s" % (number, result['domain'], result['title']))
      print("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑")
    else:
      print("%s. %s - %s" % (number, result['domain'], result['title']))