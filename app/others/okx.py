import re

import requests

URL = 'https://api.binance.com/api/v3'
URL='https://www.binance.com/api/v3/ticker/price'

response = requests.get(f'{URL}/exchangeInfo')
response = requests.get(f'{URL}')

with open('text1.json','w') as file:
    file.write(str(response.text))
res = [response.text]
# print(type(res))
res = [(response.json())]
# print(type(res))

# print(res[0]['symbol':'BLURTRY'])
symbol ='BTC'

# print(response.json())
# response = requests.get(f'{URL}/ticker/price?symbol={symbol}')

# print(response.text)
# Ваш исходный список
data = [res]
# Функция для поиска элемента по заданному значению symbol


def find_element_by_symbol(symbol_name, data_list):
    for element in data_list:
        if element["symbol"] == symbol_name:
            return element
    return None

desired_symbol = "BTCUSDT"
found_element = find_element_by_symbol(desired_symbol, data)

if found_element:
    print(found_element['price'])
    print(type(found_element))

else:
    print(f"Элемент с символом {desired_symbol} не найден.")
