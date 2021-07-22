from os import path

basedir = path.abspath(path.dirname(__file__))


class Config(object):
    DEBUG = False
    DEVELOPMENT = False
    SWAGGER = {"title": "Swagger-UI", "uiversion": 2}
    SQLALCHEMY_TRACK_MODIFICATION = False


class DevConfig(Config):
    SWAGGER = {"title": "DevSwagger-UI", "uiversion": 2}
    DEVELOPMENT = True
    DEBUG = True
    DB_SERVER = 'localhost'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/flask_app'


class TestConfig(Config):
    SWAGGER = {"title": "TestSwagger-UI", "uiversion": 2}
    WTF_CSRF_ENABLED = False
    DB_SERVER = 'localhost'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/flask_app_test'
    TESTING = True

#
# config = {
#     'dev': DevConfig,
#     'prod': TestConfig,
#     'default': DevConfig,
# }
