from flask import Flask
import random
app = Flask(__name__)


@app.route("/")
def hello():
    return "Beep Bloop Bleeeeep"


@app.route("/🤢")
def map_foo():
    return "🦖"

@app.route("/fake")
def fake():
    if random.random() < 0.5:
        return 	"😀"
    else:
        return "🙃"
