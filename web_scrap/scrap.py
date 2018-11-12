import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
# print("LLLLLLLLLL")
my_url = 'https://www.ubereats.com/en-IN/stores/'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parser
page_soup = soup(page_html, 'html.parser')







# 2419 Indore Ct, Fuquay Varina, NC, 27526