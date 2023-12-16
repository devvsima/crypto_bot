import requests

def get_user_well(user_list: int) -> str:
    URL='https://www.binance.com/api/v3/ticker/price'
    response = requests.get(URL).json() 

    text = 'Favorites:\n'
    for element in response:
        for i in user_list:
            if element["symbol"] == i:
                symbol = str(element['symbol']).replace("USDT", "")
                price = str(element['price'])[:-4]
                text += f"<blockquote>{symbol} - {price}</blockquote>\n"
    return text

def searc_coin(text: str) -> str:
    URL=f"https://api.binance.com/api/v3/ticker/price?symbol={text}"
    response = requests.get(URL).json()
    return(f"<blockquote>{(response['symbol'])[:-4]}</blockquote>\n{response['price']}")
