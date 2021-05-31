"""web app"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_app.db'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://flask_admin:admin1111@localhost:5432/flask_app"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False


MIGRATION_DIR = os.path.join('department_app/migrations')

db = SQLAlchemy(app)
migrate = Migrate(app, db, directory=MIGRATION_DIR)

import department_app.views.routes
from department_app.models.app_models import Employee, Department, Permission, Address, Location, Skill
