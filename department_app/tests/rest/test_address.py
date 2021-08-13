import unittest
from flask_fixtures import FixturesMixin

from department_app.app import create_app
from department_app.tests import AddressFactory
from department_app.database import db

app = create_app('TestingConfig')
app.app_context().push()


class TestApiAddress(unittest.TestCase, FixturesMixin):
    """Test address api class"""

    fixtures = ['address.yaml']

    app = app
    db = db

    def setUp(self):
        """setUp method"""
        self.app = app.test_client()

    def test_get_address(self):
        """Api should return information about address."""
        url = "/api/address/1"
        response = self.app.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], 1)
        self.assertEqual(response.json['name'], 'Skoriny Ul., bld. 17, appt. 12')

    def test_get_address_not_exist(self):
        """If address doesnt exist Api should return error message"""
        url = f"/api/address/999999999"
        response = self.app.get(url)
        message = f"Could not find address with ID: {999999999}."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_address_wrong_format1(self):
        """If address id have wrong format, Api should return error message"""
        url = "/api/address/one"
        response = self.app.get(url)
        message = "ID must be a number."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_address_wrong_format2(self):
        """If address id have wrong format, Api should return error message"""
        url = "/api/address/-1"
        response = self.app.get(url)
        message = "ID must be a number."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_address(self):
        """Api should update address information"""
        url = "/api/address/1"
        update_data = {'name': 'Skoriny Ul., bld. 12, appt. 17'}
        response = self.app.put(url, json=update_data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], 'Skoriny Ul., bld. 12, appt. 17')

    def test_put_address_not_exist(self):
        """Api should update address information"""
        url = "/api/address/999999999"
        update_data = {'name': 'Skoriny Ul., bld. 12, appt. 17'}
        response = self.app.put(url, json=update_data)
        message = f"Could not find address with ID: {999999999}."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_address_wrong_format1(self):
        """If address id have wrong format, Api should return error message"""
        url = "/api/address/one"
        response = self.app.put(url)
        message = "ID must be a number."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_address_wrong_format2(self):
        """If address id have wrong format, Api should return error message"""
        url = "/api/address/-1"
        response = self.app.put(url)
        message = "ID must be a number."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_address_wrong_name(self):
        """If address name have wrong format, Api should return error message"""
        url = "/api/address/1"
        update_data = {'name': 'Skoriny Ul., bld. 12, appt. 17'
                               'Skoriny Ul., bld. 12, appt. 17'
                               'Skoriny Ul., bld. 12, appt. 17'
                               'Skoriny Ul., bld. 12, appt. 17'
                               'Skoriny Ul., bld. 12, appt. 17'}
        response = self.app.put(url, json=update_data)
        message = "Exception: 1 validation error for AddressSchema\nname\n  Name length too big! (type=value_error)"

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], message)

    def test_post_address(self):
        """Api should create new address"""
        random_data = AddressFactory()
        post_data = {'name': random_data.name}
        url = "/api/address"
        response = self.app.post(url, json=post_data)

        self.assertEqual(response.status_code, 201)

    def test_post_address_wrong_name(self):
        """If address name have wrong format, Api should return error message"""
        url = "/api/address"
        post_data = {'name': 'Skoriny Ul., bld. 12, appt. 17'
                             'Skoriny Ul., bld. 12, appt. 17'
                             'Skoriny Ul., bld. 12, appt. 17'
                             'Skoriny Ul., bld. 12, appt. 17'
                             'Skoriny Ul., bld. 12, appt. 17'}
        response = self.app.post(url, json=post_data)
        message = "Exception: 1 validation error for AddressSchema\nname\n  Name length too big! (type=value_error)"

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], message)

    def test_get_address_list(self):
        """Api should return all address information"""
        url = f"/api/address"
        response = self.app.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 4)
