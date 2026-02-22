import requests
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en;q=0.9"
}
res=requests.get("https://www.amazon.in/dp/B0FGTV6BVR?aref=iIAZ6b1mnD&th=1&psc=1",headers=header)
response=res.text

soup=BeautifulSoup(response,"html.parser")
price=soup.find("span", class_="a-price-whole")
print(price.text)