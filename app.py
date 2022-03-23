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

##NEW
@app.route("/sign_up", methods=["GET, POST"])
def sign_up():
    """
    User is going to register their Account if the statements were correctly are use the word see if the current email address is already in the system or not
    """
    if request.method == "POST ":
        user = mongo.db.users
        email_address = request.form.get("email_address")
        password = request.form.get("password")
        confirmed_password = request.form.get("confirm_password")
        active_user = user.find_one({"email_Address": username.lower()})

    if active_user:
        flask("This User Email Address already exist", category="error")
        return redirect(url_for("sign_up"))

    elif len(email_Address) < 3:
        flash("Email Address must be more then 3 Characters", category="error")
        return redirect(url_for("sign_up"))

    elif len(password) < 6:
        flash("Password must be more then  Characters", category="error")
        return redirect(url_for("sign_up"))

    elif password !=confirmed_password:
        flash("Password Correct", category="error")
        return redirect(url_for("sign_up"))

    sign_up = {
        "email_address": request.form.get("email_address","username").lower(),
        "password": generate_password_hash(password, method="sha256")
    }
    
    user.insert_one(sign_up, register)

    session["email_address"] = request.form.get("email_address").lower(),
    flash("Sing UP Successfull", category = "success")
    return redirect(url_for("profile", sign_up = session["email_address"]))
           
    return render_template("sign_up.html")

@app.route("r")

  











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
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")),
        debug=True)
