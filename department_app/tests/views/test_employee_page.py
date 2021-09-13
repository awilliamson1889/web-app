import unittest

from department_app.app import create_app

app = create_app()
app.app_context().push()


class EmployeePageTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()

    def test_employee_page_get_no_information(self):
        with app.test_request_context():
            rv = self.app.get('/employee/99999999999')
            self.assertEqual(rv.request.path, '/employee/99999999999')
            self.assertEqual(rv.request.method, 'GET')
            self.assertEqual(rv.status_code, 200)

            assert 'No information about this employee!' in str(rv.data)

