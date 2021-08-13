import unittest
from flask_fixtures import FixturesMixin

from department_app.app import create_app
from department_app.tests import PermissionFactory
from department_app.database import db

app = create_app('TestingConfig')
app.app_context().push()


class TestApiPermission(unittest.TestCase, FixturesMixin):
    """Test permission api class"""

    fixtures = ['permission.yaml']

    app = app
    db = db

    def setUp(self):
        """setUp method"""
        self.app = app.test_client()

    def test_get_permission(self):
        """Api should return information about permission."""
        url = "/api/permission/1"
        response = self.app.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], 1)
        self.assertEqual(response.json['name'], 'Administrator')

    def test_get_permission_not_exist(self):
        """If permission doesnt exist Api should return error message"""
        url = f"/api/permission/999999999"
        response = self.app.get(url)
        message = f"Could not find permission with ID: {999999999}."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_permission_wrong_format1(self):
        """If permission id have wrong format, Api should return error message"""
        url = "/api/permission/one"
        response = self.app.get(url)
        message = "ID must be a number."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_permission_wrong_format2(self):
        """If permission id have wrong format, Api should return error message"""
        url = "/api/permission/-1"
        response = self.app.get(url)
        message = "ID must be a number."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_permission(self):
        """Api should update permission information"""
        url = "/api/permission/1"
        update_data = {'name': 'Viewer'}
        response = self.app.put(url, json=update_data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], 'Viewer')

    def test_put_permission_not_exist(self):
        """Api should update permission information"""
        url = "/api/permission/999999999"
        update_data = {'name': 'Viewer'}
        response = self.app.put(url, json=update_data)
        message = f"Could not find permission with ID: {999999999}."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_permission_wrong_format1(self):
        """If permission id have wrong format, Api should return error message"""
        url = "/api/permission/one"
        response = self.app.put(url)
        message = "ID must be a number."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_permission_wrong_format2(self):
        """If permission id have wrong format, Api should return error message"""
        url = "/api/permission/-1"
        response = self.app.put(url)
        message = "ID must be a number."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_permission_wrong_name(self):
        """If permission name have wrong format, Api should return error message"""
        url = "/api/permission/1"
        update_data = {'name': 'Viewer Viewer Viewer Viewer'
                               'Viewer Viewer Viewer Viewer'
                               'Viewer Viewer Viewer Viewer'
                               'Viewer Viewer Viewer Viewer'
                               'Viewer Viewer Viewer Viewer'}
        response = self.app.put(url, json=update_data)
        message = "Exception: 1 validation error for PermissionSchema\nname\n  Name length too big! (type=value_error)"

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], message)

    def test_post_permission(self):
        """Api should create new permission"""
        random_data = PermissionFactory()
        post_data = {'name': random_data.name}
        url = "/api/permission"
        response = self.app.post(url, json=post_data)

        self.assertEqual(response.status_code, 201)

    def test_post_permission_wrong_name(self):
        """If permission name have wrong format, Api should return error message"""
        url = "/api/permission"
        post_data = {'name': 'Viewer Viewer Viewer Viewer'
                             'Viewer Viewer Viewer Viewer'
                             'Viewer Viewer Viewer Viewer'
                             'Viewer Viewer Viewer Viewer'
                             'Viewer Viewer Viewer Viewer'}
        response = self.app.post(url, json=post_data)
        message = "Exception: 1 validation error for PermissionSchema\nname\n  Name length too big! (type=value_error)"

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], message)

    def test_get_permission_list(self):
        """Api should return all permission information"""
        url = f"/api/permission"
        response = self.app.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 3)
