from flask import Flask

def create_APP():
    APP = Flask(__name__)
    APP.config['SECRET_KEY'] = 'Mario.Wilson'

return APP