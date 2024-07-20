import requests
from http.client import responses

def get_exchange_info():
    url = "https://api.binance.com/api/v3/exchangeInfo"
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"ERROR: {response.status_code} {responses[response.status_code]}")
        return None

def get_order_book(symbol, limit):
    url = f"https://api.binance.com/api/v3/depth?symbol={symbol}&limit={limit}"
  
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"ERROR: {response.status_code} {responses[response.status_code]}")
        return None

def get_ticker_price(symbol):
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"ERROR: {response.status_code} {responses[response.status_code]}")
        return None