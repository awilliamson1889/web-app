from unittest.mock import patch
import unittest
from sqlalchemy.exc import IntegrityError

from department_app.app import create_app

app = create_app()
app.app_context().push()


class AddDepartmentTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()

    def test_add_department_page_get(self):
        with app.test_request_context():
            rv = self.app.get('/add/department')
            self.assertEqual(rv.request.path, '/add/department')
            self.assertEqual(rv.request.method, 'GET')
            self.assertEqual(rv.status_code, 200)

            assert '<title>Add department</title>' in str(rv.data)

    def test_add_department_post_empty_name_field(self):
        with app.test_request_context():
            rv = self.app.post('/add/department', data={'manager': 'Manager Managerov',
                                                        'date_of_creation': '1999-01-01'})
            self.assertEqual(rv.request.path, '/add/department')
            self.assertEqual(rv.request.method, 'POST')
            self.assertEqual(rv.status_code, 200)

            assert 'This field is required' in str(rv.data)
            assert '<title>Add department</title>' in str(rv.data)

    @patch('department_app.views.routes.CRUDDepartment.create', side_effect=IntegrityError('', '', ''))
    def test_add_department_post_already_exist(self, mock_create):
        with app.test_request_context():
            rv = self.app.post('/add/department', data={'name': 'very long name very long name very long name',
                                                        'manager': 'Your manager',
                                                        'date_of_creation': '1999-01-01'})

            assert 'Sorry but this department already exist.' in str(rv.data)

    @patch('department_app.views.routes.CRUDDepartment.create')
    def test_add_department_page_post(self, mock_create_department):
        mock_create_department.return_value = {'id': 1,
                                               'name': 'very long name very long name very long name',
                                               'manager': 'Your manager',
                                               'date_of_creation': '1999-01-01'}
        with app.test_request_context():
            rv = self.app.post('/add/department', data={'name': 'very long name very long name very long name',
                                                        'manager': 'Your manager',
                                                        'date_of_creation': '1999-01-01'})
            self.assertEqual(rv.request.path, '/add/department')
            self.assertEqual(rv.request.method, 'POST')
            self.assertEqual(rv.status_code, 302)

            assert '<title>Redirecting...</title>' in str(rv.data)
