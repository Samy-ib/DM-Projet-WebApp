
import os

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET') or '69trololololololololololo69_xD'
class DevelopmentConfig(Config):
    DEBUG = True
    # SECRET_KEY = '69trololololololololololo69_xD'
    ENV = "Developement"


class TestingConfig(Config):
    TESTING = True
    ENV = 'Testing'

class ProductionConfig(Config):
    ENV = 'Production'