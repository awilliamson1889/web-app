"""Rest permission Api"""
from sqlalchemy.exc import IntegrityError
from flask import Blueprint, jsonify, make_response, request
from flask_restful import Resource, Api, abort
from pydantic import ValidationError

from department_app.service import CRUDPermission
from department_app.schemas import PermissionSchema

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
        permission = CRUDPermission.get(permission_id)
        if not permission:
            return abort(404, message=f"No such permission with ID={permission_id}")
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
        permission_json = request.json

        try:
            valid_permission_json = PermissionSchema(**permission_json).dict(exclude_unset=True)
            result = CRUDPermission.update(permission_id, **valid_permission_json)
        except IntegrityError as exception:
            return abort(404, message=f"{exception}")
        except ValidationError as exception:
            return abort(404, message=f"{exception}")
        if not result:
            return abort(404, message="Permission not updated.")
        return make_response(jsonify({'message': 'Data successful updated.'}), 201)


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
        permission_json = request.json

        try:
            valid_permission_json = PermissionSchema(**permission_json).dict(exclude_unset=True)
            permission = CRUDPermission.create(**valid_permission_json)
        except IntegrityError as exception:
            return abort(404, message=f"{exception}")
        except ValidationError as exception:
            return abort(404, message=f"{exception}")
        return make_response(jsonify(permission), 201)

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
        permissions = CRUDPermission.get_permission_list()
        return make_response(jsonify(permissions), 200)


api.add_resource(PermissionList, '/api/permission')
api.add_resource(Permission, '/api/permission/<string:permission_id>')
