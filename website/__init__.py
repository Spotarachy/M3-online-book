from flask import Flask
from flash_sqlalchemy import SQLAlchemy
from os import path
bd = SQLAlchemy()
DB_NAME = "database.db"

def create_APP():
    APP = Flask(__name__)
    APP.config['SECRET_KEY'] = 'Mario Wilson'
    APP.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NANE}'

db.init_app(APP)
    
    from .views import views
    from .auth import auth

    import .Models 
    from .models import *

    APP.register_blueprint(views, url_prefix='/')
    APP.register_blueprint(auth, url_prefix='/')
    
    create_database(APP)

    return  APP
def create_database(APP):
    if not path.exists('website/ + DB_NAME'):
        db.create_all(APP=APP)
        print('Created Database!')
