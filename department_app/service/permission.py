"""Permission CRUD"""
from flask import request
from department_app.models.app_models import db, Permission, Address


class CRUDPermission:
    """Employee CRUD class"""
    @staticmethod
    def get_all_permission():
        """Get permission func"""
        permission_list = []
        permissions = Permission.query.all()
        for permission in permissions:
            permission_info = {'name': permission.name, 'permission_id': permission.id}
            permission_list.append(permission_info)
        return tuple(permission_list)

    @staticmethod
    def create_permission():
        """Create department func"""
        form_data = request.form
        permission = Permission(name=form_data['name'])
        db.session.add(permission)
        db.session.commit()
