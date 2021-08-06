"""WSGI file"""
from department_app.app import create_app

app = create_app('Prod')
