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
