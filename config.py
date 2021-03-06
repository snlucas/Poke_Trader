"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv


# Use .env file to lock SECRET KEY
#basedir = path.abspath(path.dirname(__file__))
#load_dotenv(path.join(basedir, '.env'))

# Use secrets to handle SECRET KEY
import secrets

class Config:
    """Base config"""
    #SECRET_KEY = environ.get('SECRET_KEY')
    SECRET_KEY = secrets.token_urlsafe(32)
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    #DATABASE_URI = environ.get('PROD_DATABASE_URI', '')


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = environ.get('DEV_DATABASE_URI')
