"""rest api"""
from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource, Api, abort
from pydantic import ValidationError
from department_app.models.app_models import Permission
from department_app.schemas.permission_schema import PermissionModel
from department_app.models.app_models import db


permission_api = Blueprint('permission_api', __name__)

api = Api(permission_api)


class PermissionInfo(Resource):
    """Rest class"""
    @staticmethod
    def get(permission_id):
        """
        This is the Permission API
        Call this API passing a permission_id and get back permission information
        ---
        tags:
          - Permission API
        parameters:
          - name: "permission_id"
            in: "path"
            description: "ID of permission to return"
            required: true
            type: "integer"
            format: "int64"
        responses:
          404:
            description: Could not find permission
          200:
            description: Permission information returned
        """
        if not str(permission_id).isdigit():
            abort(404, message="ID must be a number.")
        permission = Permission.query.filter_by(id=permission_id).first()
        if not permission:
            abort(404, message=f"Could not find permission with ID: {permission_id}.")
        return make_response(jsonify(permission), 200)

    @staticmethod
    def put(permission_id):
        """
        This is the Permission API
        Call this API passing a permission data and get back updated permission information
        ---
        tags:
          - Permission API
        parameters:
          - name: "permission_id"
            in: "path"
            description: "ID of permission to return"
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
                name:
                  type: "string"
                  format: "string"
                  example : "Manager"
        responses:
          404:
            description: Could not find permission
          204:
            description: Permission information successful update
        """
        if not str(permission_id).isdigit():
            abort(404, message="ID must be a number.")
        permission = Permission.query.filter_by(id=permission_id).first()
        if not permission:
            abort(404, message=f"Could not find permission with ID: {permission_id}.")

        permission_data = {'name': permission.name}

        permission_json = request.json
        permission_data.update(permission_json)

        try:
            PermissionModel(**permission_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        permission.name = permission_data['name']

        db.session.commit()
        return make_response(jsonify(permission), 201)


class AllPermissionInfo(Resource):
    """Rest class"""
    @staticmethod
    def post():
        """
        This is the Permission API
        Call this api passing a permission data and create new permission
        ---
        tags:
          - Permission API
        parameters:
          - in: "body"
            name: "POST body"
            description: "Accepts a input dictionary of inputs."
            required: true
            schema:
              type: "object"
              properties:
                name:
                  type: "string"
                  format: "string"
                  example : "Administrator"
        responses:
          201:
            description: The permission was successfully created
        """
        permission_data = {'name': request.json['name']}
        try:
            permission = PermissionModel(**permission_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        result = Permission(**permission_data)

        db.session.add(result)
        db.session.commit()
        return permission.dict(), 201

    @staticmethod
    def get():
        """
        This is the Permission API
        Call this API and get back all permissions list
        ---
        tags:
          - Permission API
        responses:
          200:
            description: All permissions returned
        """
        permissions = Permission.query.all()
        return make_response(jsonify(permissions), 200)


api.add_resource(AllPermissionInfo, '/api/permission')
api.add_resource(PermissionInfo, '/api/permission/<string:permission_id>')
