import urllib
import requests
from bs4 import BeautifulSoup

urls = "https://free-proxy-list.net/"
res = requests.get(urls)
soup = BeautifulSoup(res.text,"html.parser")


tbody = soup.find("tbody")

print(tbody.prettify())