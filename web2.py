# web2.py
#웹서버에 통신
import requests
#크롤링
from bs4 import BeautifulSoup

url = "https://www.daangn.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

posts = soup.find_all("div",attrs={"class":"card-desc"})

#파일 저장
# f = open("c:\\work\daang.txt", "wt", encoding="utf-8")
#기존 파일에 첨부(a+)
f = open("c:\\work\daang.txt", "a+", encoding="utf-8")
for post in posts:
    titleElem = post.find("h2",  attrs={"class":"card-title"})
    priceElem = post.find("div", attrs={"class":"card-price"})
    addrElem  = post.find("div", attrs={"class":"card-region-name"})
    title = titleElem.text.replace("\n","").strip()
    price = priceElem.text.replace("\n","").strip()
    addr  = addrElem.text.replace("\n","").strip()
    print(f"{title}, {price}, {addr}")
    f.write(f"{title}, {price}, {addr}\n")

f.close()