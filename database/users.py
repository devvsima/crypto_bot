from .connect import coll_users

async def get_user(id) -> None:
    return coll_users.find_one({"_id":id},{"_id":1})

async def add_user(id) -> None:
    if await get_user(id) is None: coll_users.insert_one({"_id":id, "alert":True})

async def get_users_notification() -> list:
    return coll_users.find({"alert":True},{"_id":1})

async def set_user_notification(id: int, bool: bool) -> list:
    coll_users.update_one({"_id":id},  {"$set":{"alert": bool}})

async def add_favorite_list(id, coin) -> None:
    coll_users.update_one({"_id":id},  {"$addToSet":{"list":coin}})

async def get_favorite_list(id) -> list:
    return coll_users.find_one({"_id":id},  {"_id": 0, "list":1})['list']

async def del_favorite_list_coin(id: int, coin: str) -> None:
    coll_users.update_one({"_id": id},{"$pull": {"list": coin}})