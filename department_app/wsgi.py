"""WSGI file"""
from department_app.app import create_app
import os

os.environ['FLASK_CONFIG'] = 'TestingConfig'
app = create_app(os.environ.get("FLASK_CONFIG", 'ProductionConfig'))
