import unittest
from department_app import create_app
from department_app.service.department import CRUDDepartment
from department_app.models.app_models import Department

app = create_app('Test')
app.app_context().push()


class TestDepartmentService(unittest.TestCase):
    """ doc str """
    def test_get_all_department_method(self):
        addresses_query = Department.query.all()
        addresses = CRUDDepartment.get_all_department()
        addresses_len = len(addresses_query)

        self.assertEqual(addresses_len, len(addresses))



