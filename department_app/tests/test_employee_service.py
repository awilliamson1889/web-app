import unittest
from department_app import create_app
from department_app.service.employee import CRUDEmployee
from department_app.models.app_models import Employee

app = create_app('Test')
app.app_context().push()


class TestEmployeeService(unittest.TestCase):
    """ doc str """
    def test_get_all_employee_method(self):
        employees_query = Employee.query.all()
        employees = CRUDEmployee.get_all_employee()
        employees_len = len(employees_query)

        self.assertEqual(employees_len, len(employees))
