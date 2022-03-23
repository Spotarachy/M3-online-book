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
        print("Could not connect to MongoDB: %s") % e

conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

new_doc = {"first": "max", "last": "mass", "Comic": "elastic_man", "Sub_date": "12-03-2021"}

coll.insert(new_doc)


documents = coll.find()


for doc in documents:
    print(doc)


""" Insert a single document """

#new_docs =

