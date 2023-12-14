import re
from pprint import pprint
import requests

URL='https://www.binance.com/api/v3/ticker/price'

response = requests.get(f'{URL}')
tList = ["ATOMUSDT", "BTCUSDT"]


def get_user_well(id: int):
    text = 'Favorites:\n'
    for element in response.json():
        for i in tList:
            if element["symbol"] == i:
                text += f"{element['symbol']} --- {element['price']}\n"
    return text


print(get_user_well(1))