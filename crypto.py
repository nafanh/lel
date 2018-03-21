import requests, sys, bs4, webbrowser

print('Checking...')
res = requests.get('https://coinmarketcap.com/currencies/bitcoin/')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
price =soup.find(id = 'quote_price')
print(price.get_text())
