#!/usr/bin/env python3

from flask import Flask
from model_server.frontend.index import fe
from model_server.api.index import api

app = Flask(__name__)
app.register_blueprint(fe, url_prefix='/')
app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run()
