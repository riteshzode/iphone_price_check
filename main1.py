import requests
from bs4 import BeautifulSoup
import smtplib

s = requests.Session()

product_url = "https://www.amazon.in/Apple-iPhone-13-Pro-512GB/dp/B09G9KQGJJ/ref=sr_1_2_sspa?crid=2J8J4LFF3REE5&keywords=iphone+13+pro+max&qid=1663335287&sprefix=iphone+13+pro%2Caps%2C347&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExR0ZVMTlQVjcxR01UJmVuY3J5cHRlZElkPUEwNjQ2NjcwM0MwTlM0UUo5NUhQUyZlbmNyeXB0ZWRBZElkPUEwODczMDk2M1NJU1RMWjYyOUoxMiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
r = s.get(
    url=product_url,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'})

soup = BeautifulSoup(r.content, 'html.parser')

# soup.find(name="span", class_="a-offscreen").get_text().split("₹")[1].split(".")[0]
# soup.select_one(selector=".a-offscreen").get_text().split("₹")[1].split(".")[0]

price = int(soup.select_one(selector=".a-offscreen").text.replace("₹", "").replace(",", "").split(".")[0])

if price < 150000:
    with open("file.txt", mode="r") as file:
        my_email, password = file.readlines()

    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connect:
        connect.starttls()
        connect.login(user=my_email, password=password)
        connect.sendmail(from_addr=my_email,
                         to_addrs="mrperfectritesh143@gmail.com",
                         msg=f"Subject:price alert!\n\n Check Out the price of Apple iPhone 13 Pro is less that its 1,50,000 price "
                             f"link : {product_url}")

        print("Success")
