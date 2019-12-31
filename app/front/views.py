from app.front import front
from flask import render_template

@front.route('/')
def index():
    return render_template('index.html')
