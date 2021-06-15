from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))
class Config:
    """Basic config."""
    SECRET_KEY = environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'


class ProdConfig(Config):
    """Production configuration."""
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

class DevConfig(Config):
    """Development configuration"""
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True