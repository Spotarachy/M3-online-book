from os
import path 
import pymongo
from flask import (
     Flask, render_template, url_for, request, redirect)
from .env import MONGO_URI 
from flask_login import UserMixin
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__, template_folder="website/template")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
MONGO = PyMongo(app)

#NEW
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "my1DB"
COLLECTION = "ArtBook"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


#DB_NAME = "database.db"

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/")
def index():
    """
        Will take a user to the index page.
            """

    ArtBook = MONGO.db.ArtBook.insert_one({
    'first': 'Junji',
    'last': 'Ito',
    'comic_name': 'Uzumaki',
    'Language': 'Japanese',
    'page_numbers': '1043',
    'date_sub': '31/01/2020'
})
    print(ArtBook)
    return render_template("base.html",)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")


@app.errorhandler(500)
def server_error(e):
    """
        If the page doesn't load, the user will see this message.
            """
    return render_template("500.html")

@app.errorhandler(404)
def server_error(e):
    """
        If the page doesn't load, the user will see this message.
            """
    return render_template("404.html")


if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")),
        debug=True)
