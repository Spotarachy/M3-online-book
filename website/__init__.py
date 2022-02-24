from flask import Flask

def create_APP():
    (Flask(__name__)).config['SECRET_KEY'] = 'Mario Wilson'
    
    from .views import views
    from .auth import auth

    app.register_Blueprint(views, url_prefix='/')
    app.register_Blueprint(auth, url_prefix='/')

    return Flask(__name__)