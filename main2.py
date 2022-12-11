import requests
from bs4 import BeautifulSoup

product_url = "https://www.amazon.in/dp/B0BDJH6GL8"

s = requests.Session()

r = s.get(url=product_url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'})

soup = BeautifulSoup(r.content, 'html.parser')

# print(soup.prettify())
price = soup.find(name="span", class_="a-offscreen").text.split(".")[0]

print(f"The price of Apple iPhone 14 Pro Max 128GB is {price}")

