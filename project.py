from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


URL = 'https://www.amazon.com/pack-Coffee-Paper-Disposable-white/dp/B09SCW7Y8N/ref=sr_1_3_sspa?crid=2A9EXP1G835N5&keywords=cup&qid=1676279672&sprefix=cu%2Caps%2C568&sr=8-3-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyTkZMTFc4Tjg1NkxOJmVuY3J5cHRlZElkPUEwNTYwMjUzMUJXVzY5NTJQRk9KVCZlbmNyeXB0ZWRBZElkPUEwMDY2MjM0MzFXVDVLWTZXTkpQQyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='




headers = "headers = {\"User-Agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36\", \"Accept-Encoding\":\"gzip, deflate\", \"Accept\":\"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\", \"DNT\":\"1\",\"Connection\":\"close\", \"Upgrade-Insecure-Requests\":\"1\"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

price = soup2.find(id='priceblock_ourprice').get_text()

price = price.strip()[1:]
title = title.strip()

import datetime

today = datetime.date.today()

import csv

header = ['Title', 'Price', 'Date']
data = [title, price, today]

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


while(True):
    check_price()
    time.sleep(86400)






