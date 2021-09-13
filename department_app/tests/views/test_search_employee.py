import unittest

from department_app.app import create_app

app = create_app()
app.app_context().push()


class SearchEmployeeTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()

    def test_search_employee_page_get(self):
        with app.test_request_context():
            rv = self.app.get('/search/employee')
            self.assertEqual(rv.request.path, '/search/employee')
            self.assertEqual(rv.request.method, 'GET')
            self.assertEqual(rv.status_code, 200)

            assert '<title>People search</title>' in str(rv.data)

    def test_search_employee_page_post(self):
        with app.test_request_context():
            rv = self.app.post('/search/employee')
            self.assertEqual(rv.request.path, '/search/employee')
            self.assertEqual(rv.request.method, 'POST')
            self.assertEqual(rv.status_code, 200)

            assert '<title>People search</title>' in str(rv.data)