from flask import Flask

def create_APP():
    (Flask(__name__)).config['SECRET_KEY'] = 'Mario Wilson'
    
    from .views import views
    from .auth import auth

    APP.register_blueprint(views, url_prefix='/')
    APP.register_blueprint(auth, url_prefix='/')

    return  APP
