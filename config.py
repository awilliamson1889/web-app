import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/flask_app'
    SWAGGER = {"title": "DevSwagger-UI", "uiversion": 2}


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/flask_prod"
    DEBUG = False
    CONFIG_NAME = 'Prod'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/flask_dev"
    DEVELOPMENT = True
    DEBUG = True
    CONFIG_NAME = 'Dev'


class TestingConfig(Config):
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/flask_test"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///flask_app.db'
    TESTING = True
    CONFIG_NAME = 'Test'
