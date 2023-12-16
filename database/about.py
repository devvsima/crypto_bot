from .connect import coll_about

async def add_about_coin(coin, text) -> None:
    try: coll_about.insert_one({"coin": coin, "text": text})
    except: coll_about.update_search_index({"coin": coin}, {"text": text})

async def get_about_coin(coin) -> str:
    return coll_about.find_one({"coin":coin}, {"_id": 0, "coin": 0})['text']


async def get_coins_list() -> list:
    return coll_about.distinct("coin")
    


