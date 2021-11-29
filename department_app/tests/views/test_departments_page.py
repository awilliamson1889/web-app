import unittest

from department_app.app import create_app

app = create_app()
app.app_context().push()


class DepartmentsPageTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()

    def test_departments_page_post(self):
        with app.test_request_context():
            rv = self.app.post('/departments')
            self.assertEqual(rv.request.path, '/departments')
            self.assertEqual(rv.request.method, 'POST')
            self.assertEqual(rv.status_code, 200)

            assert '<title>Departments</title>' in str(rv.data)

    def test_departments_page_get(self):
        with app.test_request_context():
            rv = self.app.get('/departments')
            self.assertEqual(rv.request.path, '/departments')
            self.assertEqual(rv.request.method, 'GET')
            self.assertEqual(rv.status_code, 200)

            assert '<title>Departments</title>' in str(rv.data)
