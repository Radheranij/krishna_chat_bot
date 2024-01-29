from pymongo import MongoClient

import config

Krishna db = MongoClient(config.MONGO_URL)
Krishna = Krishna db["Krishna Db"]["Krishna"]


from .chats import *
from .users import *
