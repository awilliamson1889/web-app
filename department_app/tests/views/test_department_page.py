import unittest

from department_app.app import create_app

app = create_app()
app.app_context().push()


class DepartmentPageTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()

    def test_department_page_get_no_information(self):
        with app.test_request_context():
            rv = self.app.get('/department/99999999999')
            self.assertEqual(rv.request.path, '/department/99999999999')
            self.assertEqual(rv.request.method, 'GET')
            self.assertEqual(rv.status_code, 200)

            assert 'No information about this department' in str(rv.data)

    def test_manage_department_page_get(self):
        with app.test_request_context():
            rv = self.app.get('/manage/department')
            self.assertEqual(rv.request.path, '/manage/department')
            self.assertEqual(rv.request.method, 'GET')
            self.assertEqual(rv.status_code, 200)

            assert 'Manage department' in str(rv.data)
