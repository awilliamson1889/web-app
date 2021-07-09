"""rest api"""
from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource, Api, abort
from department_app.models.app_models import Employee
from department_app.models.employee_schema import EmployeeModel
from department_app.models.app_models import db
from pydantic import ValidationError

employee_api = Blueprint('employee_api', __name__)

api = Api(employee_api)


class EmployeeInfo(Resource):
    def get(self, employee_id):
        """
        This is the Employee API
        Call this API passing a employee_id and get back employee information
        ---
        tags:
          - Employee API
        parameters:
          - name: "employee_id"
            in: "path"
            description: "ID of department to return"
            required: true
            type: "integer"
            format: "int64"
        responses:
          404:
            description: Could not find department
          200:
            description: Department information returned
        """
        if not str(employee_id).isdigit():
            abort(404, message=f"ID must be a number.")
        employee = Employee.query.filter_by(id=employee_id).first()
        if not employee:
            abort(404, message=f"Could not find employee with ID: {employee_id}.")
        return make_response(jsonify(employee), 200)

    def put(self, employee_id):
        """
        This is the Employee API
        Call this API passing a employee data and get back updated employee information
        ---
        tags:
          - Employee API
        parameters:
          - name: "employee_id"
            in: "path"
            description: "ID of pet to return"
            required: true
            type: "integer"
            format: "int64"
          - in: "body"
            name: "PUT body"
            description: "Accepts a input dictionary of inputs."
            required: true
            schema:
              type: "object"
              properties:
                date_of_birth:
                  type: "string"
                  format: "string"
                  example : "1999-12-12"
                date_of_joining:
                  type: "string"
                  format: "string"
                  example : "2021-12-12"
                department:
                  type: "int"
                  format: "int64"
                  example : 1
                email:
                  type: "string"
                  format: "string"
                  example : "andy_b@mymail.com"
                key_skill:
                  type: "int"
                  format: "int64"
                  example : 1
                location:
                  type: "int"
                  format: "int64"
                  example : 1
                name:
                  type: "string"
                  format: "string"
                  example : "Andy"
                phone:
                  type: "string"
                  format: "string"
                  example : "3752900000000"
                salary:
                  type: "float"
                  format: "float64"
                  example : 2000.50
                surname:
                  type: "string"
                  format: "string"
                  example : "Bes"
                work_address:
                  type: "string"
                  format: "string"
                  example : 1
                permission:
                  type: "string"
                  format: "string"
                  example : 1
        responses:
          404:
            description: Could not find employee
          204:
            description: Employee information successful update
        """
        if not str(employee_id).isdigit():
            abort(404, message=f"ID must be a number.")
        employee = Employee.query.filter_by(id=employee_id).first()
        if not employee:
            abort(404, message=f"Could not find employee with ID: {employee_id}.")

        if 'name' in request.json:
            employee.name = request.json['name']
        if 'surname' in request.json:
            employee.surname = request.json['surname']
        if 'date_of_birth' in request.json:
            employee.date_of_birth = request.json['date_of_birth']
        if 'salary' in request.json:
            employee.salary = request.json['salary']
        if 'email' in request.json:
            employee.email = request.json['email']
        if 'phone' in request.json:
            employee.phone = request.json['phone']
        if 'date_of_joining' in request.json:
            employee.date_of_joining = request.json['date_of_joining']
        if 'department' in request.json:
            employee.department = request.json['department']
        if 'location' in request.json:
            employee.location = request.json['location']
        if 'work_address' in request.json:
            employee.work_address = request.json['work_address']
        if 'key_skill' in request.json:
            employee.key_skill = request.json['key_skill']
        if 'permission' in request.json:
            employee.permission = request.json['permission']
        try:
            result = EmployeeModel(id=employee.id, name=employee.name, surname=employee.surname,
                                   date_of_birth=str(employee.date_of_birth), salary=employee.salary,
                                   email=employee.email, phone=employee.phone,
                                   date_of_joining=str(employee.date_of_joining), department=employee.department,
                                   location=employee.location, work_address=employee.work_address,
                                   key_skill=employee.key_skill, permission=employee.permission)
        except ValidationError as e:
            abort(404, message=f"Exception: {e}")

        db.session.commit()
        return result.dict(), 204

    def delete(self, employee_id):
        """
        This is the Employee API
        Call this API passing a employee_id and delete this employee
        ---
        tags:
          - Employee API
        parameters:
          - name: "employee_id"
            in: "path"
            description: "ID of employee to delete"
            required: true
            type: "integer"
            format: "int64"
        responses:
          404:
            description: Could not find employee
          200:
            description: Employee deleted
        """
        if not str(employee_id).isdigit():
            abort(404, message=f"ID must be a number.")
        employee = Employee.query.filter_by(id=employee_id).first()
        if not employee:
            abort(404, message=f"Could not find employee with ID: {employee_id}.")
        db.session.delete(employee)
        db.session.commit()
        return '', 204


class AllEmployeeInfo(Resource):
    def post(self):
        """
        This is the Employee API
        Call this api passing a employee data and create new employee
        ---
        tags:
          - Employee API
        parameters:
          - in: "body"
            name: "POST body"
            description: "Accepts a input dictionary of inputs."
            required: true
            schema:
              type: "object"
              properties:
                date_of_birth:
                  type: "string"
                  format: "string"
                  example : "1999-12-12"
                date_of_joining:
                  type: "string"
                  format: "string"
                  example : "2021-12-12"
                department:
                  type: "int"
                  format: "int64"
                  example : 1
                email:
                  type: "string"
                  format: "string"
                  example : "andy_b@mymail.com"
                key_skill:
                  type: "int"
                  format: "int64"
                  example : 1
                location:
                  type: "int"
                  format: "int64"
                  example : 1
                name:
                  type: "string"
                  format: "string"
                  example : "Andy"
                phone:
                  type: "string"
                  format: "string"
                  example : "3752900000000"
                salary:
                  type: "float"
                  format: "float64"
                  example : 2000.50
                surname:
                  type: "string"
                  format: "string"
                  example : "Bes"
                work_address:
                  type: "string"
                  format: "string"
                  example : 1
                permission:
                  type: "string"
                  format: "string"
                  example : 1
        responses:
          201:
            description: The employee was successfully created
        """
        employee = Employee.query.all()
        employee_data = {'id': len(employee)+100, 'name': request.json['name'], 'surname': request.json['surname'],
                         'date_of_birth': request.json['date_of_birth'], 'salary': request.json['salary'],
                         'email': request.json['email'], 'phone': request.json['phone'],
                         'date_of_joining': request.json['date_of_joining'], 'department': request.json['department'],
                         'location': request.json['location'], 'work_address': request.json['work_address'],
                         'key_skill': request.json['key_skill'], 'permission': request.json['permission']}
        try:
            employees = EmployeeModel(**employee_data)
        except ValidationError as e:
            abort(404, message=f"Exception: {e}")

        result = Employee(**employee_data)

        db.session.add(result)
        db.session.commit()
        return employees.dict(), 201

    def get(self):
        """
        This is the Employee API
        Call this API and get back all employees list
        ---
        tags:
          - Employee API
        responses:
          200:
            description: All employees returned
        """
        employee = Employee.query.all()
        return make_response(jsonify(employee), 200)

api.add_resource(EmployeeInfo, '/api/employee/<string:employee_id>')
api.add_resource(AllEmployeeInfo, '/api/employee')
