import unittest

from department_app.app import create_app

app = create_app()
app.app_context().push()


class ManageEmployeeTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()

    def test_manage_employee_page_get(self):
        with app.test_request_context():
            rv = self.app.get('/manage/employee')
            self.assertEqual(rv.request.path, '/manage/employee')
            self.assertEqual(rv.request.method, 'GET')
            self.assertEqual(rv.status_code, 200)

            assert 'Manage employee' in str(rv.data)

    def test_manage_employee_page_post(self):
        with app.test_request_context():
            rv = self.app.post('/manage/employee')
            self.assertEqual(rv.request.path, '/manage/employee')
            self.assertEqual(rv.request.method, 'POST')
            self.assertEqual(rv.status_code, 200)

            assert 'Manage employee' in str(rv.data)
