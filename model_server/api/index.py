import random
import sys

import pandas as pd
from flask import Blueprint, request
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.externals import joblib


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
    return str(model.predict(
        pd.DataFrame(

            {
                'title': [request.form['Title']],
                'text': [request.form['Text']]
            }
        )
    )[0])
