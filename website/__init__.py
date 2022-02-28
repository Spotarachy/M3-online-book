from flask import Flask
from flash_sqlalchemy import SQLAlchemy

bd = SQLAlchemy()
DB_NAME = "database.db"

def create_APP():
    APP = Flask(__name__)
    APP.config['SECRET_KEY'] = 'Mario Wilson'
    APP.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NANE}'

db.init_app(APP)
    
    from .views import views
    from .auth import auth

    APP.register_blueprint(views, url_prefix='/')
    APP.register_blueprint(auth, url_prefix='/')

    return  APP
