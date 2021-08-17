"""App config"""
import os
from dotenv import load_dotenv


load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SWAGGER = {"title": "DevSwagger-UI", "uiversion": 2}


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"{os.environ.get('DB_DRIVER')}://{os.environ.get('DB_USER_NAME')}:" \
                              f"{os.environ.get('DB_PASSWORD')}@{os.environ.get('DB_HOST')}:" \
                              f"{os.environ.get('DB_PORT')}" \
                              f"/{os.environ.get('DB_NAME')}"
    DEBUG = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/flask_dev"
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/flask_test"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///flask_app.db'
    TESTING = True
