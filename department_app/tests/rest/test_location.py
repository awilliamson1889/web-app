import unittest
from flask_fixtures import FixturesMixin

from department_app.app import create_app
from department_app.tests import LocationFactory
from department_app.database import db

app = create_app('TestingConfig')
app.app_context().push()


class TestApiLocation(unittest.TestCase, FixturesMixin):
    """Test location api class"""

    fixtures = ['location.yaml']

    app = app
    db = db

    def setUp(self):
        """setUp method"""
        self.app = app.test_client()

    def test_get_location(self):
        """Api should return information about location."""
        url = "/api/location/1"
        response = self.app.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], 1)
        self.assertEqual(response.json['name'], 'Bobruysk')

    def test_get_location_not_exist(self):
        """If location doesnt exist Api should return error message"""
        url = f"/api/location/999999999"
        response = self.app.get(url)
        message = f"Could not find location with ID: {999999999}."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_location_wrong_format1(self):
        """If location id have wrong format, Api should return error message"""
        url = "/api/location/one"
        response = self.app.get(url)
        message = "ID must be a number."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_location_wrong_format2(self):
        """If location id have wrong format, Api should return error message"""
        url = "/api/location/-1"
        response = self.app.get(url)
        message = "ID must be a number."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_location(self):
        """Api should update location information"""
        url = "/api/location/1"
        update_data = {'name': 'Brest'}
        response = self.app.put(url, json=update_data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], 'Brest')

    def test_put_location_not_exist(self):
        """Api should update location information"""
        url = "/api/location/999999999"
        update_data = {'name': 'Brest'}
        response = self.app.put(url, json=update_data)
        message = f"Could not find location with ID: {999999999}."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_location_wrong_format1(self):
        """If location id have wrong format, Api should return error message"""
        url = "/api/location/one"
        response = self.app.put(url)
        message = "ID must be a number."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_location_wrong_format2(self):
        """If location id have wrong format, Api should return error message"""
        url = "/api/location/-1"
        response = self.app.put(url)
        message = "ID must be a number."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_location_wrong_name(self):
        """If location name have wrong format, Api should return error message"""
        url = "/api/location/1"
        update_data = {'name': 'Bobruysk Bobruysk Bobruysk Bobruysk'
                               'Bobruysk Bobruysk Bobruysk Bobruysk'
                               'Bobruysk Bobruysk Bobruysk Bobruysk'
                               'Bobruysk Bobruysk Bobruysk Bobruysk'
                               'Bobruysk Bobruysk Bobruysk Bobruysk'}
        response = self.app.put(url, json=update_data)
        message = "Exception: 1 validation error for LocationSchema\nname\n  Name length too big! (type=value_error)"

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], message)

    def test_post_location(self):
        """Api should create new location"""
        random_data = LocationFactory()
        post_data = {'name': random_data.name}
        url = "/api/location"
        response = self.app.post(url, json=post_data)

        self.assertEqual(response.status_code, 201)

    def test_post_location_wrong_name(self):
        """If location name have wrong format, Api should return error message"""
        url = "/api/location"
        post_data = {'name': 'Bobruysk Bobruysk Bobruysk Bobruysk'
                             'Bobruysk Bobruysk Bobruysk Bobruysk'
                             'Bobruysk Bobruysk Bobruysk Bobruysk'
                             'Bobruysk Bobruysk Bobruysk Bobruysk'
                             'Bobruysk Bobruysk Bobruysk Bobruysk'}
        response = self.app.post(url, json=post_data)
        message = "Exception: 1 validation error for LocationSchema\nname\n  Name length too big! (type=value_error)"

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], message)

    def test_get_location_list(self):
        """Api should return all location information"""
        url = f"/api/location"
        response = self.app.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 4)
