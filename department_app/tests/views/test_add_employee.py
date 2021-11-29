import unittest

from department_app.app import create_app

app = create_app()
app.app_context().push()


class AddEmployeeTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()

    def test_add_employee_page_get(self):
        with app.test_request_context():
            rv = self.app.get('/add/employee')
            self.assertEqual(rv.request.path, '/add/employee')
            self.assertEqual(rv.request.method, 'GET')
            self.assertEqual(rv.status_code, 200)

            assert '<title>Add employee</title>' in str(rv.data)

    def test_add_employee_page_post_empty_fields(self):
        with app.test_request_context():
            rv = self.app.post('/add/employee')
            self.assertEqual(rv.request.path, '/add/employee')
            self.assertEqual(rv.request.method, 'POST')
            self.assertEqual(rv.status_code, 200)

            assert 'This field is required' in str(rv.data)
            assert '<title>Add employee</title>' in str(rv.data)
