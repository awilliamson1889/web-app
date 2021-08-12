"""Permission CRUD"""
from sqlalchemy.exc import IntegrityError
from flask import request
from flask_restful import abort
from department_app.models import PermissionModel
from department_app.database import db


class CRUDPermission:
    """Employee CRUD class"""
    @staticmethod
    def get_permission(permission_id):
        """Get permission func"""
        if not str(permission_id).isdigit():
            abort(404, message="ID must be a number.")
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
    def update_permission(permission_id, json):
        """update permission func"""
        permission = PermissionModel.query.filter_by(id=permission_id).first()
        permission.name = json['name']

        try:
            db.session.commit()
        except IntegrityError as exception:
            abort(404, message=f"Exception: {exception}")
        return permission

    @staticmethod
    def create_permission(form=None):
        """Create department func"""
        if form:
            permission = PermissionModel(name=form.name.data)
        else:
            permission = PermissionModel(name=request.json['name'])

        try:
            db.session.add(permission)
            db.session.commit()
        except IntegrityError as exception:
            abort(404, message=f"Exception: {exception}")
