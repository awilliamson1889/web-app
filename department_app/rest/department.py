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
    def get_json():
        """Get address json, if json have wrong format - return abort """
        try:
            department_json = {'name': request.json['name'],
                               'date_of_creation': request.json['date_of_creation'],
                               'manager': request.json['manager']}
        except KeyError:
            return False
        return department_json

    @staticmethod
    def json_is_valid(json) -> bool:
        """Validate address json data, if json data not valid - return abort"""
        try:
            DepartmentSchema(**json)
        except ValidationError:
            return False
        return True

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
        if str(department_id).isdigit() and int(department_id) > 0:
            department = CRUDDepartment.get(department_id)
        else:
            abort(404, message="Invalid ID format!")
        if not department:
            abort(404, message=f"No such department with ID={department_id}")
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
        department_json = Department.get_json()
        if not department_json:
            abort(404, message="Wrong JSON fields names.")

        if not Department.json_is_valid(department_json):
            abort(404, message="JSON is not valid.")
        try:
            result = CRUDDepartment.update(department_id, name=department_json['name'],
                                           date_of_creation=department_json['date_of_creation'],
                                           manager=department_json['manager'])
        except IntegrityError as exception:
            abort(404, message=f"{exception}")
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
        department_json = Department.get_json()
        if not department_json:
            abort(404, message="Wrong JSON fields names.")

        if not Department.json_is_valid(department_json):
            abort(404, message="JSON is not valid.")
        try:
            department = CRUDDepartment.create(**department_json)
        except IntegrityError as exception:
            abort(404, message=f"{exception}")
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
