import os
from flask import Flask

APP = Flask(__name__)

@app.route('/')
def index():
    return "Hello,world"

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        prot=int(os.environ.geet("PORT", "5000")),
        debug=True)
