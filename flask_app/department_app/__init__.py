"""create app"""
from flask import Flask
import department_app.views.views
app = Flask(__name__)
