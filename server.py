#!/usr/bin/env python3

from flask import Flask
from model_server.frontend.index import fe
from model_server.api.index import api
from model_server.database import db


app = Flask(__name__, template_folder='model_server/templates/', static_folder='model_server/static')
app.register_blueprint(fe, url_prefix='/')
app.register_blueprint(api, url_prefix='/api')

db.init_app(app)

if __name__ == '__main__':
    app.run()
