"""Permission CRUD"""
from sqlalchemy.exc import IntegrityError
from pydantic import ValidationError
from flask_restful import abort
from flask import request

from department_app.schemas import PermissionSchema
from department_app.models import PermissionModel
from department_app.database import db
from .service import check_id_format


class CRUDPermission:
    """Employee CRUD class"""
    @staticmethod
    def get_permission(permission_id):
        """Get permission func"""
        check_id_format(permission_id)
        permission = PermissionModel.query.filter_by(id=permission_id).first()
        if not permission:
            abort(404, message=f"Could not find permission with ID: {permission_id}.")
        return permission

    @staticmethod
    def get_all_permission():
        """Get permission func"""
        permission_list = []
        permissions = PermissionModel.query.all()
        for permission in permissions:
            permission_info = {'name': permission.name, 'permission_id': permission.id}
            permission_list.append(permission_info)
        return tuple(permission_list)

    @staticmethod
    def update_permission(permission_id):
        """update permission func"""
        permission = CRUDPermission.get_permission(permission_id)

        permission_data = {'name': permission.name}

        permission_json = request.json
        permission_data.update(permission_json)

        try:
            PermissionSchema(**permission_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        permission.name = permission_data['name']

        try:
            db.session.commit()
        except IntegrityError as exception:
            abort(404, message=f"Exception: {exception}")
        return permission

    @staticmethod
    def create_permission(form=None):
        """Create department func"""
        if form:
            permission_data = {'name': form.name.data}
            permission = PermissionModel(**permission_data)
        else:
            permission_data = {'name': request.json['name']}
            permission = PermissionModel(**permission_data)

        try:
            PermissionSchema(**permission_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        try:
            db.session.add(permission)
            db.session.commit()
        except IntegrityError as exception:
            abort(404, message=f"Exception: {exception}")

        return permission
