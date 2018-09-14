from flask import Flask
from flask import request
app = Flask(__name__)


@app.route("/")
def hello():
    return "Beep Bloop Bleeeeep"


@app.route("/🤢")
def map_foo():
    return "🦖"

@app.route("/fake")
def fake():
    return request.args.get('news', '')
