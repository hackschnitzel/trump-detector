from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

fe = Blueprint('frontend', __name__,
               template_folder='templates')


@fe.route('/', defaults={'page': 'index'})
@fe.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)