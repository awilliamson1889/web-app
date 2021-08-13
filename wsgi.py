"""WSGI file"""
import os
from department_app.app import create_app
from department_app.database import db


app = create_app(os.environ.get("FLASK_CONFIG", 'ProductionConfig'))

db.init_app(app)
with app.app_context():
    db.create_all()
    db.session.commit()
