from website import db
from flask_login import UserMixin

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
