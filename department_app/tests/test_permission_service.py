import unittest
from department_app import create_app
from department_app.service.permission import CRUDPermission
from department_app.models.app_models import Permission

app = create_app('Test')
app.app_context().push()


class TestPermissionService(unittest.TestCase):
    """ doc str """
    def test_get_all_permission_method(self):
        permission_query = Permission.query.all()
        permissions = CRUDPermission.get_all_permission()
        permission_len = len(permission_query)

        self.assertEqual(permission_len, len(permissions))
