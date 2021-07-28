"""rest api"""
from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource, Api, abort
from pydantic import ValidationError
from department_app.models.app_models import Department
from department_app.schemas.department_schema import DepartmentModel
from department_app.models.app_models import db

department_api = Blueprint('department_api', __name__)

api = Api(department_api)


class DepartmentInfo(Resource):
    """Rest class"""
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
        if not str(department_id).isdigit():
            abort(404, message="ID must be a number.")
        department = Department.query.filter_by(id=department_id).first()
        if not department:
            abort(404, message=f"Could not find department with ID: {department_id}.")
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
        if not str(department_id).isdigit():
            abort(404, message="ID must be a number.")
        department = Department.query.filter_by(id=department_id).first()
        if not department:
            abort(404, message=f"Could not find department with ID: {department_id}.")

        department_data = {'name': department.name, 'date_of_creation': department.date_of_creation,
                           'manager': department.manager}

        department_json = request.json
        department_data.update(department_json)

        try:
            DepartmentModel(**department_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        department.name = department_data['name']
        department.manager = department_data['manager']
        department.date_of_creation = department_data['date_of_creation']

        db.session.commit()
        return make_response(jsonify(department), 201)


class AllDepartmentInfo(Resource):
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
        department_data = {'name': request.json['name'], 'manager': request.json['manager'],
                           'date_of_creation': request.json['date_of_creation']}
        try:
            department = DepartmentModel(**department_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        result = Department(**department_data)

        db.session.add(result)
        db.session.commit()
        return department.dict(), 201

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
        departments = Department.query.all()
        return make_response(jsonify(departments), 200)


api.add_resource(AllDepartmentInfo, '/api/department')
api.add_resource(DepartmentInfo, '/api/department/<string:department_id>')
