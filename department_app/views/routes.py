"""Routes web-app"""
from flask import Blueprint
from department_app.models.app_models import Employee


from flask import Blueprint, request, jsonify, make_response, render_template
from flask_restful import Resource, Api, abort
from pydantic import ValidationError
from department_app.models.app_models import Employee
from department_app.models.employee_schema import EmployeeModel
from department_app.models.app_models import db
from department_app.service.employee import CRUDEmployee


frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    """Return / page"""
    db.session.commit()
    return str("R")


@frontend.route('/form')
def form():
    return render_template('form.html')


@frontend.route('/form2')
def form2():
    employee = CRUDEmployee.get_employee(employee_id=1)
    return render_template('form2.html', employee=employee)


@frontend.route('/create/employee', methods=['POST', 'GET'])
def create_employee():
    """Return / page"""
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        CRUDEmployee.create_employee()
        return "DATA ADDED"


@frontend.route('/update/employee', methods=['POST', 'GET'])
def update_employee():
    """Return / page"""
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        CRUDEmployee.update_employee(1)
        return "DATA UPDATED"
