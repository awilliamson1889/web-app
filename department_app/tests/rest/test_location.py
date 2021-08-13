import os
import unittest
from flask_fixtures import FixturesMixin
from department_app.app import create_app
from department_app.models import LocationModel
from department_app.tests import LocationFactory
from department_app.database import db


os.environ['FLASK_CONFIG'] = 'TestingConfig'
app = create_app(os.environ.get("FLASK_CONFIG", 'ProductionConfig'))
app.app_context().push()


class TestApiLocation(unittest.TestCase, FixturesMixin):
    """ doc str """

    fixtures = ['location.yaml']

    app = app
    db = db

    def setUp(self):
        """ doc str """
        self.app = app.test_client()

    def test_get_location(self):
        location = LocationModel.query.order_by(LocationModel.id).all()
        last_location = location[-1]
        url = f"/api/location/{last_location.id}"
        client = app.test_client()
        response = client.get(url)

        self.assertEqual(200, response.status_code)
        self.assertEqual(last_location.id, response.json['id'])
        self.assertEqual(last_location.name, response.json['name'])

    def test_get_location_not_exist(self):
        location_id = 999999999
        client = app.test_client()
        url = f"/api/location/{location_id}"
        message = f"Could not find location with ID: {location_id}."
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_str_id_format(self):
        location_id = "one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/location/{location_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_negative_num_id_format(self):
        location_id = -1
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/location/{location_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_str_num_id_format(self):
        location_id = "1one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/location/{location_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_float_num_id_format(self):
        location_id = 1.0
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/location/{location_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_location(self):
        location = LocationModel.query.order_by(LocationModel.id).all()
        client = app.test_client()
        last_location = location[-1]
        update_test_data = {'name': 'update_test_location'}
        url = f"/api/location/{last_location.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(201, response.status_code)
        self.assertEqual(last_location.id, response.json['id'])
        self.assertEqual(update_test_data['name'], response.json['name'])

    def test_put_location_not_exist(self):
        location_id = 999999999
        client = app.test_client()
        url = f"/api/location/{location_id}"
        message = f"Could not find location with ID: {location_id}."
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_str_id_format(self):
        location_id = "one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/location/{location_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_negative_num_id_format(self):
        location_id = -1
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/location/{location_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_str_num_id_format(self):
        location_id = "1one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/location/{location_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_float_num_id_format(self):
        location_id = 1.0
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/location/{location_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_big_location_name(self):
        location = LocationModel.query.order_by(LocationModel.id).all()
        last_emp = location[-1]
        client = app.test_client()
        update_test_data = {'name': 'test_very_big_location_name_test_very_big_location_name_very_big_location_name_'
                                    'test_very_big_location_name_test_very_big_location_name_test_very_big_name'}
        message = "Exception: 1 validation error for LocationSchema\nname\n  Name length too big! (type=value_error)"
        url = f"/api/location/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    # def test_put_location_already_exist(self):
    #     location = LocationModel.query.order_by(LocationModel.id).all()
    #     client = app.test_client()
    #     last_location = location[-1]
    #     update_test_data = {'name': last_location.name}
    #     message = "Exception: 1 validation error for LocationSchema\n" \
    #               "name\n  This location is already in use! (type=value_error)"
    #     url = f"/api/location/{last_location.id}"
    #     response = client.put(url, json=update_test_data)
    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(message, response.json['message'])

    def test_post_location(self):
        test_location = LocationFactory()
        client = app.test_client()
        test_data = {'name': test_location.name}
        url = f"/api/location"
        response = client.post(url, json=test_data)
        self.assertEqual(response.status_code, 201)
        emp = LocationModel.query.order_by(LocationModel.id).all()
        last_emp = emp[-1]
        db.session.delete(last_emp)
        db.session.commit()

    def test_get_location_all(self):
        url = f"/api/location"
        client = app.test_client()
        response = client.get(url)
        location = LocationModel.query.order_by(LocationModel.id).all()
        self.assertEqual(len(response.json), len(location))

    def test_post_location_very_long_name(self):
        client = app.test_client()
        test_data = {'name': 'test_very_big_location_name_test_very_big_location_name_very_big_location_name_'
                             'test_very_big_location_name_test_very_big_location_name_test_very_big_name'}
        message = "Exception: 1 validation error for LocationSchema\nname\n  Name length too big! (type=value_error)"
        url = f"/api/location"
        response = client.post(url, json=test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])