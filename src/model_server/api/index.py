from flask import Blueprint

api = Blueprint('api', __name__,
                template_folder='templates')


@api.route("/")
def hello():
    return "Beep Bloop Bleeeeep"


@api.route("/🤢")
def map_foo():
    return "🦖"


@api.route("/check", methods=["POST"])
def check():
    if request.form['news'] == 'covfefe':
        return '1.0'
    else:
        return str(random.random())
