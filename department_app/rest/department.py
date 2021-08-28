"""Rest department Api"""
from sqlalchemy.exc import IntegrityError
from flask import Blueprint, jsonify, make_response, request
from flask_restful import Resource, Api, abort
from pydantic import ValidationError

from department_app.service import CRUDDepartment
from department_app.schemas import DepartmentSchema


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
        department = CRUDDepartment.get(department_id)
        if not department:
            return abort(404, message=f"No such department with ID={department_id}")
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
        department_json = request.json

        try:
            valid_department_json = DepartmentSchema(**department_json).dict(exclude_unset=True)
            result = CRUDDepartment.update(department_id, **valid_department_json)
        except IntegrityError as exception:
            return abort(404, message=f"Department {exception}")
        except ValidationError as exception:
            return abort(404, message=f"Department {exception}")
        if not result:
            return abort(404, message="Department not updated.")
        return make_response(jsonify({'message': 'Data successful updated.'}), 201)


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
        department_json = request.json

        try:
            valid_department_json = DepartmentSchema(**department_json).dict(exclude_unset=True)
            department = CRUDDepartment.create(**valid_department_json)
        except IntegrityError as exception:
            return abort(404, message=f"Department {exception}")
        except ValidationError as exception:
            return abort(404, message=f"Department {exception}")
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
        departments = CRUDDepartment.get_department_list()
        return make_response(jsonify(departments), 200)


api.add_resource(DepartmentList, '/api/department')
api.add_resource(Department, '/api/department/<string:department_id>')
