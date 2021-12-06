import requests
from bs4 import BeautifulSoup
import time

EURO_RUB = 'https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%B2+%D1%80%D1%83%D0%B1%D0%BB%D0%B8&oq=%D0%B5%D0%B2%D1%80%D0%BE+%D0%B2+%D1%80%D1%83%D0%B1%D0%BB%D0%B8&aqs=chrome..69i57.2835j0j9&client=ms-android-samsung-ss&sourceid=chrome-mobile&ie=UTF-8'
DOLLAR_RUB = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&aqs=chrome..69i57.3017j0j7&client=ms-android-samsung-ss&sourceid=chrome-mobile&ie=UTF-8'
BITCOIN_RUB = 'https://www.google.com/search?q=%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD+%D0%B2+%D1%80%D1%83%D0%B1%D0%BB%D0%B8&oq=%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD+%D0%B2+%D1%80%D1%83%D0%B1%D0%BB%D0%B8&aqs=chrome..69i57.3741j0j7&client=ms-android-samsung-ss&sourceid=chrome-mobile&ie=UTF-8'


user = "Mozilla/5.0 (Linux; Android 11; SM-A515F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 GoogleApp/12.47.14.23.arm64"
header = {'User-Agent':user}

def requests_f(currency): 
    return requests.get(currency, headers = header)
    
def beautiSoup(currency):
    return BeautifulSoup(currency.content, 'html.parser')
    
def check_currency():
    full_page_euro = requests_f(EURO_RUB)
    full_page_dollar = requests_f(DOLLAR_RUB)
    full_page_bitcoin = requests_f(BITCOIN_RUB)
    
    euro_soup = beautiSoup(full_page_euro)
    dollar_soup = beautiSoup(full_page_dollar)
    bitcoin_soup = beautiSoup(full_page_bitcoin)
    
    euro_price = euro_soup.findAll('span', {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    dollar_price = dollar_soup.findAll('span', {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    bitcoin_price = bitcoin_soup.findAll('span', {"class":"pclqee"})
    
    euro_last_update = euro_soup.findAll('div', {"class": "hqAUc"})
    dollar_last_update = dollar_soup.findAll('div', {"class": "hqAUc"})
    bitcoin_last_update = bitcoin_soup.findAll('div', {"class":"ciceSb"})
    
    print("\n1 евро = " + euro_price[0].text + "р  " + euro_last_update[0].text[:-26])
    print("1 доллар = " + dollar_price[0].text + "р  " + dollar_last_update[0].text[:-26])
    print("1 биткоин = " + bitcoin_price[0].text + "р  " + bitcoin_last_update[0].text[:-26])
    
    time.sleep(5)
    check_currency()
    
check_currency()
