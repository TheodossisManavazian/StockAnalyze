import requests
from bs4 import BeautifulSoup

ticker = input("Enter Ticker: ")
response = requests.get('https://www.marketwatch.com/investing/stock/' + ticker)
soup = BeautifulSoup(response.text, 'html.parser')


def getPrice():
    pr = soup.find('bg-quote', class_="value")
    price = pr.get_text()
    return price


def getKeyData():
    keyData = []
    kd = soup.findAll('span', class_='kv__value kv__primary')
    for index in kd:
        keyData.append(index.get_text())

    return keyData


print(ticker)
print(getPrice())
print(getKeyData())