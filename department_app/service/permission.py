"""Permission CRUD"""
from department_app.models.app_models import db, Permission


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
    def create_permission(form):
        """Create department func"""
        permission = Permission(name=form.name.data)
        db.session.add(permission)
        db.session.commit()
