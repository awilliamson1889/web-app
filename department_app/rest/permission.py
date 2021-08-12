"""Rest permission Api"""
from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource, Api, abort
from pydantic import ValidationError
from department_app.schemas import PermissionSchema
from department_app.service import CRUDPermission

permission_api = Blueprint('permission_api', __name__)

api = Api(permission_api)


class Permission(Resource):
    """Permission API class"""
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
        permission = CRUDPermission.get_permission(permission_id)
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
        permission = CRUDPermission.get_permission(permission_id)

        permission_data = {'name': permission.name}

        permission_json = request.json
        permission_data.update(permission_json)

        try:
            PermissionSchema(**permission_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        CRUDPermission.update_permission(permission_id, permission_data)

        return make_response(jsonify(permission), 201)


class PermissionList(Resource):
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
            permission = PermissionSchema(**permission_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        CRUDPermission.create_permission()

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
        permissions = CRUDPermission.get_all_permission()
        return make_response(jsonify(permissions), 200)


api.add_resource(PermissionList, '/api/permission')
api.add_resource(Permission, '/api/permission/<string:permission_id>')
