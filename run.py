from flask import Flask, render_template
import config 
from app.api import api
app = Flask(__name__)

app.config.from_object(config.DevelopmentConfig)
app.register_blueprint(api)

@app.route('/')
def index():
    return 'In developement'

if __name__ == '__main__':
  app.run()
 