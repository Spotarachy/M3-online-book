import os
from flask import Flask, render_template
from flash_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask import Blueprint, render_template, request, flask, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from .Models import User
from . import db

bd = SQLAlchemy()
DB_NAME = "database.db"

app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("home.html")


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


class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    data = bd.Column(bd.String(10000))
    data = db.Column(db.DataTime(timezone=True), default=func.now())
    user_id =db.Column(db.Integer, db.ForeingKey('user.id'))

class image(bd.Model, UserMixin):
    id =db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_Name =db.Column(db.String(150))
    notes = db.relationship('Note')


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_Name =db.Column(db.String(150))
    notes = db.relationship('Note')


bd = SQLAlchemy()
DB_NAME = "database.db"



app = Blueprint('app', __name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
    data = request.form
    return render_template("login.html", boolean=True)

@app.route('/logout')
def logout():
    return "<p>Logout</p>" 

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = reques.form.get('firstName')
        password1 = reques.form.get('password1')
        password2 = reques.form.get('password2')

    if len(email) < 4:
        pass
    elif len(first_name) < 2:
        pass
    elif password1 != password2:
        pass
    elif len(password1) < 6:
        pass
    else:
        #add user to database

    if len(email) < 4:
        flask('Email cant less then 3 chararcters.'category='Oops')
    elif len(first_name) < 2:
        flask('firstName cant less then 1 chararcters.'category='Oops Sorry')
        
    elif password1 != password2:
        flask('password don\'t match.'category='Oops')

    elif len(password1) < 6:
        flask('Email cant less then 6 chararcters.'category='Oops Sorry')

    else:
        new_user = (email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))

        db.session.add(new_user)
        db.session.commit()
        flash('Accoount created!', category='success')
        return redirect(url_for('views.home'))
    
        #add user to database
return render_template("sign_up.html")

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Mario Wilson'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NANE}'

db.init_app(app)
    

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')
    
create_database(APP)


return app
def create_database(APP):
    if not path.exists('website/ + DB_NAME'):
        db.create_all(APP=APP)
        print('Created Database!')
