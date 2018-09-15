import sqlite3
import sys

import pandas as pd
from flask import Blueprint, request, jsonify, Response
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.externals import joblib

from model_server.database import db


class Selector(BaseEstimator, TransformerMixin):
    def __init__(self, cols):
        self.cols = cols

    def fit(self, X, y=None):
        return X

    def transform(self, X):
        return X[self.cols]

    def fit_transform(self, X, y=None):
        return self.transform(X)


setattr(
    sys.modules['__main__'],
    'Selector',
    Selector)
model = joblib.load('Keramik/nn.pkl')

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
    score = model.predict_proba(
        pd.DataFrame(

            {
                'title': [request.form['Title']],
                'text': [request.form['Text']]
            }
        )
    )[0][0]
    return jsonify({"score": score})


@api.route("/label", methods=["POST"])
def label():
    is_fake = 1 if request.form['Fake'] else 0
    title = request.form['Title']
    text = request.form['Text']

    statement = "INSERT INTO articles (title, text, fake) VALUES (?, ?, ?)"

    database_conn = db.get_db()
    cursor = database_conn.cursor()
    cursor.execute(statement, (title, text, is_fake))
    database_conn.commit()
    database_conn.close()
    return Response(status=204)
