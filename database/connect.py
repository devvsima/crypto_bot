from pymongo import MongoClient
from data.config import mongodb_url

client = MongoClient(mongodb_url)
db = client["crypto_bot"]

coll_users = db.users