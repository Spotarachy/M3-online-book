import os
import pymongo
from flask import (
     Flask, render_template, url_for, request, redirect, flash, session)
##from .env import MONGO_URI 
from flask_login import UserMixin
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from os import path
if os.path.exists("env.py"):
    import env

app = Flask(__name__, template_folder="template")

app.config["MONGO_URI"] = 'mongodb+srv://M3:python21@xo21.hjgyv.mongodb.net/?retryWrites=true&w=majority'

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

MONGO = PyMongo(app)

os.environ['MONGO_URI'] = 'mongodb+srv://M3:Spotarachy21Ronin@xo21.hjgyv.mongodb.net/my1DB?retryWrites=true&w=majority'

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

@app.route("/")
def index():
    """
    Will take a user to the index page.
    """
    return render_template("index.html",)

##New
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Allow users to log into their existing account, the function is to see if the username or email address already exists in the database and add accordingly to tell users this person already exists.
    """
    print(request.method)

    if request.method == "POST":
        user = mongo.db.users
        current_user = user.find_one({"email_address": request.form.get().lower()})
        if check_password_hash (current_user["password"],request.form.get("password")):session["email_address"] = request.form.get("email_address","username").lower()
        return(url_for("profile", sign_up=session["email_address"]))

    else:
        Flask("The User/Email is not Correct")
        return redirect(url_for("login"))

    return render_template("login.html")

##NEW


@app.route("/add_comic", methods=["GET","POST"])
def add_comic():
    return render_template('add_comics.html')













@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    """
    User is going to register their Account if the statements were correctly are use the word see if the current email address is already in the system or not
    """
    print(request.method)

    if request.method == "POST":
        user = MONGO.db.user
        email_address = request.form.get("email")
        password = request.form.get("password1")
        confirmed_password = request.form.get("password2")
        active_user = user.find_one({"email_Address":email_address})
        print(email_address, password)

        if active_user:
            flash("This User Email Address already exist", category="error")
            print('taking')
            return redirect(url_for("sign_up"))

        elif len(email_address) < 3:
            flash("Email Address must be more then 3 Characters", category="error")
            print('true')
            return redirect(url_for("sign_up"))

        elif len(password) < 6:
            flash("Password must be more then  Characters", category="error")
            return redirect(url_for("sign_up"))

        #this was commited out\/
        elif password !=confirmed_password:
            flash("Password Correct", category="error")
            return redirect(url_for("sign_up"))

        sign_up = {
            "email_address": request.form.get("email").lower(),
            "password": generate_password_hash(password, method="sha256")
        }
        
        user.insert_one(sign_up)

        session["email_address"] = request.form.get("email").lower(), flash("Sing UP Success full", category = "success")
      
    return redirect(url_for("index", sign_up=session["email_address"]))
        
    return render_template("sign_up.html")


## NEW
##comic_id if needed    \/
@app.route("/delete/comic_id")
def delete (comic_id):
    mongo.db.comic.remove({"_id": ObjectId(comic_id)})
    flask("Your Comic has been Deleted")
    return redirect(url_for("index.html"))

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
##

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
