from flask import Blueprint

api = Blueprint('api', __name__, template_folder='templates', url_prefix='/api', static_folder='static')

from app.api import views