import unittest

from department_app.app import create_app

app = create_app()
app.app_context().push()


class ManageDepartmentTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()

    def test_manage_department_page_get(self):
        with app.test_request_context():
            rv = self.app.get('/manage/department')
            self.assertEqual(rv.request.path, '/manage/department')
            self.assertEqual(rv.request.method, 'GET')
            self.assertEqual(rv.status_code, 200)

            assert 'Manage department' in str(rv.data)
