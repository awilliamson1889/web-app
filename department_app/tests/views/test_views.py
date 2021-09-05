from unittest.mock import patch, Mock
import unittest
from flask import Flask, request
from sqlalchemy.exc import IntegrityError

from department_app.app import create_app

app = create_app()
app.app_context().push()


class ViewsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()

    def test_add_address_page_get(self):
        with app.test_request_context():
            rv = self.app.get('/add/address')
            self.assertEqual(rv.request.path, '/add/address')
            self.assertEqual(rv.request.method, 'GET')
            self.assertEqual(rv.status_code, 200)

            assert '<title>Add address</title>' in str(rv.data)

    def test_add_address_page_post_empty_name_field(self):
        with app.test_request_context():
            rv = self.app.post('/add/address')
            self.assertEqual(rv.request.path, '/add/address')
            self.assertEqual(rv.request.method, 'POST')
            self.assertEqual(rv.status_code, 200)

            assert 'This field is required' in str(rv.data)
            assert '<title>Add address</title>' in str(rv.data)

    def test_add_address_page_post_very_long_name(self):
        """Api should return information about address."""
        with app.test_request_context():
            rv = self.app.post('/add/address', data={'name': 'very long name very long name very long name'
                                                             'very long name very long name very long name'
                                                             'very long name very long name very long name'
                                                             'very long name very long name very long name'
                                                             'very long name very long name very long name'})

            assert 'Address length must be between 3 and 100 characters' in str(rv.data)

    @patch('department_app.views.routes.CRUDAddress.create', side_effect=IntegrityError('', '', ''))
    def test_add_address_page_post_already_exist(self, mock_create):
        """Api should return information about address."""
        with app.test_request_context():
            rv = self.app.post('/add/address', data={'name': 'very long name very long name very long name'})

            assert 'Sorry but this address already exist.' in str(rv.data)

    def test_add_location_page_get(self):
        with app.test_request_context():
            rv = self.app.get('/add/location')
            self.assertEqual(rv.request.path, '/add/location')
            self.assertEqual(rv.request.method, 'GET')
            self.assertEqual(rv.status_code, 200)

            assert '<title>Add location</title>' in str(rv.data)

    def test_add_location_page_post_empty_name_field(self):
        with app.test_request_context():
            rv = self.app.post('/add/location')
            self.assertEqual(rv.request.path, '/add/location')
            self.assertEqual(rv.request.method, 'POST')
            self.assertEqual(rv.status_code, 200)

            assert 'This field is required' in str(rv.data)
            assert '<title>Add location</title>' in str(rv.data)

    def test_add_location_page_post_very_long_name(self):
        """Api should return information about address."""
        with app.test_request_context():
            rv = self.app.post('/add/location', data={'name': 'very long name very long name very long name'
                                                              'very long name very long name very long name'
                                                              'very long name very long name very long name'
                                                              'very long name very long name very long name'
                                                              'very long name very long name very long name'})

            assert 'Location length must be between 3 and 100 characters' in str(rv.data)

    @patch('department_app.views.routes.CRUDLocation.create', side_effect=IntegrityError('', '', ''))
    def test_add_location_page_post_already_exist(self, mock_create):
        with app.test_request_context():
            rv = self.app.post('/add/location', data={'name': 'very long name very long name very long name'})

            assert 'Sorry but this location already exist.' in str(rv.data)

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

    def test_add_skill_page_get(self):
        with app.test_request_context():
            rv = self.app.get('/add/skill')
            self.assertEqual(rv.request.path, '/add/skill')
            self.assertEqual(rv.request.method, 'GET')
            self.assertEqual(rv.status_code, 200)

            assert '<title>Add skill</title>' in str(rv.data)

    def test_add_skill_page_post_empty_name_field(self):
        with app.test_request_context():
            rv = self.app.post('/add/skill')
            self.assertEqual(rv.request.path, '/add/skill')
            self.assertEqual(rv.request.method, 'POST')
            self.assertEqual(rv.status_code, 200)

            assert 'This field is required' in str(rv.data)
            assert '<title>Add skill</title>' in str(rv.data)

    def test_add_skill_page_post_very_long_name(self):
        """Api should return information about address."""
        with app.test_request_context():
            rv = self.app.post('/add/skill', data={'name': 'very long name very long name very long name'
                                                           'very long name very long name very long name'
                                                           'very long name very long name very long name'
                                                           'very long name very long name very long name'
                                                           'very long name very long name very long name'})

            assert 'Skill length must be between 3 and 50 characters' in str(rv.data)

    @patch('department_app.views.routes.CRUDSkill.create', side_effect=IntegrityError('', '', ''))
    def test_add_skill_page_post_already_exist(self, mock_create):
        with app.test_request_context():
            rv = self.app.post('/add/skill', data={'name': 'very long name very long name very long name'})

            assert 'Sorry but this skill already exist.' in str(rv.data)

    def test_add_department_page_get(self):
        with app.test_request_context():
            rv = self.app.get('/add/department')
            self.assertEqual(rv.request.path, '/add/department')
            self.assertEqual(rv.request.method, 'GET')
            self.assertEqual(rv.status_code, 200)

            assert '<title>Add department</title>' in str(rv.data)

    def test_add_department_page_post_empty_name_field(self):
        with app.test_request_context():
            rv = self.app.post('/add/department', data={'manager': 'Manager Managerov',
                                                        'date_of_creation': '1999-01-01'})
            self.assertEqual(rv.request.path, '/add/department')
            self.assertEqual(rv.request.method, 'POST')
            self.assertEqual(rv.status_code, 200)

            assert 'This field is required' in str(rv.data)
            assert '<title>Add department</title>' in str(rv.data)

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