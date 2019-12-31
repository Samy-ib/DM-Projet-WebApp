from flask import Flask, render_template
import config 
from app.api import api
from app.front import front

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        variable_start_string='[[',  # Default is '{{', I'm changing this because Vue.js uses '{{' / '}}'
        variable_end_string=']]',
    ))


app = CustomFlask(__name__, static_folder = './app/front/static')

app.config.from_object(config.DevelopmentConfig)
app.register_blueprint(api)
app.register_blueprint(front)


# @app.route('/')
# def index():
#     return 'In developement'

if __name__ == '__main__':
  app.run()
 