import re
from pprint import pprint
import requests

def searc_coin(text):
    URL=f"https://api.binance.com/api/v3/ticker/price?symbol={text}"
    try:
        response = requests.get(URL).json()
        return(f"{response['symbol']} - {response['price']}")
    except:
        return("Coin nor found!\nTry again.")

