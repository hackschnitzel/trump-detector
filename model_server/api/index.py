import sys
from flask import Blueprint, request
import random

from sklearn.externals import joblib

from sklearn.base import BaseEstimator, TransformerMixin


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
    import pandas as pd
    if request.form['news'] == 'covfefe':
        return '1.0'
    else:
        return str(model.predict(
            pd.DataFrame(

                    {
                        'title': ['Kerry to go to Paris in gesture of sympathy'],
                        'text': [
                            '''
U.S. Secretary of State John F. Kerry said Monday that he will stop in Paris later this week, amid criticism that no top American officials attended Sunday’s unity march against terrorism.

Kerry said he expects to arrive in Paris Thursday evening, as he heads home after a week abroad. He said he will fly to France at the conclusion of a series of meetings scheduled for Thursday in Sofia, Bulgaria. He plans to meet the next day with Foreign Minister Laurent Fabius and President Francois Hollande, then return to Washington.

The visit by Kerry, who has family and childhood ties to the country and speaks fluent French, could address some of the criticism that the United States snubbed France in its darkest hour in many years.

The French press on Monday was filled with questions about why neither President Obama nor Kerry attended Sunday’s march, as about 40 leaders of other nations did. Obama was said to have stayed away because his own security needs can be taxing on a country, and Kerry had prior commitments.

Among roughly 40 leaders who did attend was Israeli Prime Minister Benjamin Netanyahu, no stranger to intense security, who marched beside Hollande through the city streets. The highest ranking U.S. officials attending the march were Jane Hartley, the ambassador to France, and Victoria Nuland, the assistant secretary of state for European affairs. Attorney General Eric H. Holder Jr. was in Paris for meetings with law enforcement officials but did not participate in the march.

Kerry spent Sunday at a business summit hosted by India’s prime minister, Narendra Modi. The United States is eager for India to relax stringent laws that function as barriers to foreign investment and hopes Modi’s government will act to open the huge Indian market for more American businesses.

In a news conference, Kerry brushed aside criticism that the United States had not sent a more senior official to Paris as "quibbling a little bit." He noted that many staffers of the American Embassy in Paris attended the march, including the ambassador. He said he had wanted to be present at the march himself but could not because of his prior commitments in India.

"But that is why I am going there on the way home, to make it crystal clear how passionately we feel about the events that have taken place there," he said.

"And I don’t think the people of France have any doubts about America’s understanding of what happened, of our personal sense of loss and our deep commitment to the people of France in this moment of trauma."
                            ''']
                    }
            )
        )[0])
        return str(random.random())
