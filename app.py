from os import path 
if path.exists("env.py"):
    import env
from flask import Flask, render_template
from .env import MONGO_URI 
from flask_login import UserMixin
from flask import url_for 
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
# from .app import User
# from . import db.   


app = Flask(__name__, template_folder='website/template')


app.config['MONGO_URI'] = os.environ.get('MONGO_URI')


DB_NAME = "database.db"


MONGO = PyMongo(app)


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/")
def index():
    ArtBook = MONGO.db.ArtBook.insert_one({
    'first': 'Junji',
    'last': 'Ito',
    'comic_name': 'Uzumaki',
    'Language': 'Japanese',
    'page_numbers': '1043',
    'date_sub': '31/01/2020'
})
    print(ArtBook)
    return render_template("base.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
