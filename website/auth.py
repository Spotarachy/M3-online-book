import os
from flask import Blueprint, render_template, request, flask, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from .Models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
    data = request.form
    return render_template("login.html", boolean=True)

@auth.route('/logout')
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
