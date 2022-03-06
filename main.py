import os
from flask import Flask, render_template

APP = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html")


@app.route("/addcomics")
def addcomics():
    return render_template("addcomics.html")


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/sign_up")
def sign_up():
    return render_template("sing_up.html")



if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        prot=int(os.environ.geet("PORT", "5000")),
        debug=True)
