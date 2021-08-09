"""WSGI file"""
from department_app import create_app

# app = create_app('Prod')
app = create_app('Test')

if __name__ == "main":
    app.run()
