"""Rest employee Api"""
from flask import Blueprint, jsonify, make_response
from flask_restful import Resource, Api

from department_app.service import CRUDEmployee

employee_api = Blueprint('employee_api', __name__)

api = Api(employee_api)


class Employee(Resource):
    """Employee API class"""
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
        employee = CRUDEmployee.get_employee(employee_id)
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
        employee = CRUDEmployee.update_employee(employee_id)
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
        CRUDEmployee.delete_employee(employee_id)
        return '', 204


class EmployeeList(Resource):
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
        employee = CRUDEmployee.create_employee()
        return make_response(jsonify(employee), 201)

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
        employee = CRUDEmployee.get_all_employee()
        return make_response(jsonify(employee), 200)


api.add_resource(Employee, '/api/employee/<string:employee_id>')
api.add_resource(EmployeeList, '/api/employee')
