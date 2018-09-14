from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Beep Bloop Bleeeeep"


@app.route("/🤢")
def ggg():
    return "🦖"