"""rest api"""
from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource, Api, abort
from pydantic import ValidationError
from department_app.models.app_models import Employee
from department_app.models.schemas.employee_schema import EmployeeModel
from department_app.models.app_models import db

employee_api = Blueprint('employee_api', __name__)

api = Api(employee_api)


class EmployeeInfo(Resource):
    """Rest class"""
    @staticmethod
    def get(employee_id):
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
            abort(404, message="ID must be a number.")
        employee = Employee.query.filter_by(id=employee_id).first()
        if not employee:
            abort(404, message=f"Could not find employee with ID: {employee_id}.")
        return make_response(jsonify(employee), 200)

    @staticmethod
    def put(employee_id):
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
          201:
            description: Employee information successful update
        """
        if not str(employee_id).isdigit():
            abort(404, message="ID must be a number.")
        employee = Employee.query.filter_by(id=employee_id).first()
        if not employee:
            abort(404, message=f"Could not find employee with ID: {employee_id}.")

        employee_data = {'name': employee.name, 'surname': employee.surname,
                         'date_of_birth': str(employee.date_of_birth), 'salary': employee.salary,
                         'email': employee.email, 'phone': employee.phone,
                         'date_of_joining': str(employee.date_of_joining), 'department': employee.department,
                         'location': employee.location, 'work_address': employee.work_address,
                         'key_skill': employee.key_skill, 'permission': employee.permission}

        employee_json = request.json
        employee_data.update(employee_json)

        try:
            EmployeeModel(**employee_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        employee.name = employee_data['name']
        employee.surname = employee_data['surname']
        employee.date_of_birth = employee_data['date_of_birth']
        employee.salary = employee_data['salary']
        employee.email = employee_data['email']
        employee.phone = employee_data['phone']
        employee.date_of_joining = employee_data['date_of_joining']
        employee.department = employee_data['department']
        employee.location = employee_data['location']
        employee.work_address = employee_data['work_address']
        employee.key_skill = employee_data['key_skill']
        employee.permission = employee_data['permission']
        db.session.commit()
        return make_response(jsonify(employee), 201)

    @staticmethod
    def delete(employee_id):
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
          204:
            description: Employee deleted
        """
        if not str(employee_id).isdigit():
            abort(404, message="ID must be a number.")
        employee = Employee.query.filter_by(id=employee_id).first()
        if not employee:
            abort(404, message=f"Could not find employee with ID: {employee_id}.")
        db.session.delete(employee)
        db.session.commit()
        return '', 204


class AllEmployeeInfo(Resource):
    """Rest class"""
    @staticmethod
    def post():
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
        employee_data = {'name': request.json['name'], 'surname': request.json['surname'],
                         'date_of_birth': request.json['date_of_birth'], 'salary': request.json['salary'],
                         'email': request.json['email'], 'phone': request.json['phone'],
                         'date_of_joining': request.json['date_of_joining'], 'department': request.json['department'],
                         'location': request.json['location'], 'work_address': request.json['work_address'],
                         'key_skill': request.json['key_skill'], 'permission': request.json['permission']}
        try:
            employees = EmployeeModel(**employee_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        result = Employee(**employee_data)

        db.session.add(result)
        db.session.commit()
        return employees.dict(), 201

    @staticmethod
    def get():
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