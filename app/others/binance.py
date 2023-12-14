import requests


tList = ["ATOMUSDT", "BTCUSDT"] 

def get_user_well(user_id: int) -> str:
    URL='https://www.binance.com/api/v3/ticker/price'
    response = requests.get(URL).json() 

    text = 'Favorites:\n'
    for element in response:
        for i in tList:
            if element["symbol"] == i:
                text += f"{element['symbol']} --- {element['price']}\n"
    return text

def searc_coin(text: str) -> str:
    URL=f"https://api.binance.com/api/v3/ticker/price?symbol={text}"
    response = requests.get(URL).json()
    return(f"{response['symbol']} - {response['price']}")
