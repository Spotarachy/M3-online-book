import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "my1DB"
COLLECTION = "ArtBook"

