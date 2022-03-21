import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "my1DB"
COLLECTION = "ArtBook"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connected: %s") % e
        

conn = mongo_connect(MONGO_URI)

Spotarachy21Ronin
coll = conn[DATABASE][COLLECTION]


documents = coll.find()


for doc in documents:
    print(ok)


""" Insert a single document """
