from flask import Blueprint

front = Blueprint('front', __name__, template_folder='templates', url_prefix='', static_folder='static')

from app.front import views