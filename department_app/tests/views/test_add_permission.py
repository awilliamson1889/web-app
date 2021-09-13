from unittest.mock import patch
import unittest
from sqlalchemy.exc import IntegrityError

from department_app.app import create_app

app = create_app()
app.app_context().push()


class AddPermissionTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()
        
    def test_add_permission_page_get(self):
        with app.test_request_context():
            rv = self.app.get('/add/permission')
            self.assertEqual(rv.request.path, '/add/permission')
            self.assertEqual(rv.request.method, 'GET')
            self.assertEqual(rv.status_code, 200)

            assert '<title>Add permission</title>' in str(rv.data)

    def test_add_permission_page_post_empty_name_field(self):
        with app.test_request_context():
            rv = self.app.post('/add/permission')
            self.assertEqual(rv.request.path, '/add/permission')
            self.assertEqual(rv.request.method, 'POST')
            self.assertEqual(rv.status_code, 200)

            assert 'This field is required' in str(rv.data)
            assert '<title>Add permission</title>' in str(rv.data)

    @patch('department_app.views.routes.CRUDPermission.create')
    def test_add_permission_page_post(self, mock_create):
        mock_create.return_value = {'id': 1,
                                    'name': 'name'}
        with app.test_request_context():
            rv = self.app.post('/add/permission', data={'name': 'name'})
            self.assertEqual(rv.request.path, '/add/permission')
            self.assertEqual(rv.request.method, 'POST')
            self.assertEqual(rv.status_code, 302)

            assert '<title>Redirecting...</title>' in str(rv.data)

    def test_add_permission_page_post_very_long_name(self):
        """Api should return information about address."""
        with app.test_request_context():
            rv = self.app.post('/add/permission', data={'name': 'very long name very long name very long name'
                                                                'very long name very long name very long name'
                                                                'very long name very long name very long name'
                                                                'very long name very long name very long name'
                                                                'very long name very long name very long name'})

            assert 'Permission length must be between 3 and 50 characters' in str(rv.data)

    @patch('department_app.views.routes.CRUDPermission.create', side_effect=IntegrityError('', '', ''))
    def test_add_permission_page_post_already_exist(self, mock_create):
        with app.test_request_context():
            rv = self.app.post('/add/permission', data={'name': 'very long name very long name very long name'})

            assert 'Sorry but this permission already exist.' in str(rv.data)
