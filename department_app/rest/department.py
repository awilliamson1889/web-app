"""Rest department Api"""
from flask import Blueprint, jsonify, make_response
from flask_restful import Resource, Api

from department_app.service import CRUDDepartment


department_api = Blueprint('department_api', __name__)

api = Api(department_api)


class Department(Resource):
    """Department API class"""
    @staticmethod
    def get(department_id):
        """
        This is the Department API
        Call this API passing a department_id and get back department information
        ---
        tags:
          - Department API
        parameters:
          - name: "department_id"
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
        department = CRUDDepartment.get_department(department_id)
        return make_response(jsonify(department), 200)

    @staticmethod
    def put(department_id):
        """
        This is the Department API
        Call this API passing a department data and get back updated department information
        ---
        tags:
          - Department API
        parameters:
          - name: "department_id"
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
                date_of_creation:
                  type: "string"
                  format: "string"
                  example : "2021-12-12"
                manager:
                  type: "string"
                  format: "string"
                  example : "Ivanka Adamson"
                name:
                  type: "string"
                  format: "string"
                  example : "RD Lab Brest"
        responses:
          404:
            description: Could not find department
          204:
            description: Department information successful update
        """
        department = CRUDDepartment.update_department(department_id)
        return make_response(jsonify(department), 201)


class DepartmentList(Resource):
    """Rest class"""
    @staticmethod
    def post():
        """
        This is the Department API
        Call this api passing a department data and create new department
        ---
        tags:
          - Department API
        parameters:
          - in: "body"
            name: "POST body"
            description: "Accepts a input dictionary of inputs."
            required: true
            schema:
              type: "object"
              properties:
                date_of_creation:
                  type: "string"
                  format: "string"
                  example : "2021-12-12"
                manager:
                  type: "string"
                  format: "string"
                  example : "Ivanka Adamson"
                name:
                  type: "string"
                  format: "string"
                  example : "RD Lab Brest"
        responses:
          201:
            description: The department was successfully created
        """
        department = CRUDDepartment.create_department()
        return make_response(jsonify(department), 201)

    @staticmethod
    def get():
        """
        This is the Department API
        Call this API and get back all departments list
        ---
        tags:
          - Department API
        responses:
          200:
            description: All department returned
        """
        departments = CRUDDepartment.get_all_department()
        return make_response(jsonify(departments), 200)


api.add_resource(DepartmentList, '/api/department')
api.add_resource(Department, '/api/department/<string:department_id>')
