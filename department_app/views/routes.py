"""Routes web-app"""
from flask import Blueprint, jsonify
from department_app.models.app_models import Employee, Department

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    employees = Employee.query.filter_by(key_skill=1)
    dep = Department.query.all()
    emp = Employee.query.all()
    a = str([x.phone for x in emp])
    b = str([ix.phone for ix in employees])
    return str([x.name for x in dep])
