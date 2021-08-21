"""Permission CRUD"""
import logging
from sqlalchemy.exc import IntegrityError

from department_app.models import PermissionModel
from department_app.database import db


class CRUDPermission:
    """Permission CRUD class"""
    @staticmethod
    def get(permission_id):
        """Get permission func"""
        logging.info("Get permission method called with parameters: id=%s", permission_id)

        permission = PermissionModel.query.filter_by(id=permission_id).first()

        if not permission:
            return None
        return permission

    @staticmethod
    def update(permission_id, name):
        """Update permission func"""
        logging.info("Update permission method called with parameters: id=%s, name=%s.", permission_id, name)

        try:
            result = PermissionModel.query.where(PermissionModel.id == permission_id). \
                update({PermissionModel.name: name})
            db.session.commit()
        except IntegrityError as exception:
            logging.info("Permission with name=%s already exist.", name)
            raise exception
        return bool(result)

    @staticmethod
    def get_permission_list():
        """Get location func"""
        permissions = PermissionModel.query.all()

        if len(permissions) > 0:
            return tuple(({'name': permission.name,
                           'id': permission.id} for permission in permissions))
        return []

    @staticmethod
    def create(name):
        """Create permission func"""
        logging.info("Create permission method called with parameters: name=%s.", name)

        permission = PermissionModel(name=name)

        try:
            db.session.add(permission)
            db.session.commit()
        except IntegrityError as exception:
            logging.info("Permission with name=%s already exist.", name)
            raise exception
        return permission
