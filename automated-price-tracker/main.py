import smtplib
import requests
from bs4 import BeautifulSoup
import lxml
import os

my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("MY_PWD")
receiver = os.environ.get("MY_EMAIL2")
url = "https://www.amazon.com/Wacom-Graphics-Animation-Beginners-DTC133W0A/dp/B082LZXQ6B/ref=sr_1_12?qid=1672849451&rnid=172456&s=electronics&sr=1-12"
name = "Wacom-Graphics-Animation"
treshold = 400

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.5",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
}
response = requests.get(
    url=url,
    headers=headers,
)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")
price = float(
    (soup.select_one(".a-price-whole")).getText()
    + (soup.select_one(".a-price-fraction")).getText()
)

if price < treshold:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver,
            msg=f"Subject:{name} price Alert!\n\n{name} is now listed under ${treshold}!\n{url}",
        )
