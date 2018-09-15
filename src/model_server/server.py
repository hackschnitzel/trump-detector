from flask import Flask
from flask import request
import random
app = Flask(__name__)


@app.route("/")
def hello():
    return "Beep Bloop Bleeeeep"


@app.route("/🤢")
def map_foo():
    return "🦖"

@app.route("/check", methods=["POST"])
def check():
    if request.form['news'] == 'covfefe':
        return '1.0'
    else:
        return str(random.random())
