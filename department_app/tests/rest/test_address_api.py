import unittest
from department_app import create_app
from department_app.models.app_models import db, Address
from department_app.tests.factories.address_factory import AddressFactory

app = create_app('Test')
app.app_context().push()


class TestApiAddress(unittest.TestCase):
    """Test address api class"""
    def setUp(self):
        """setUp method"""
        self.app = app.test_client()
        test_address = AddressFactory()
        test_data = {'name': test_address.name}
        address = Address(**test_data)
        db.session.add(address)
        db.session.commit()
        db.create_all()

    def tearDown(self):
        """tearDown method"""
        address = Address.query.order_by(Address.id).all()
        db.session.delete(address[-1])
        db.session.commit()

    def test_get_address(self):
        """Api should return information about address."""
        address = Address.query.order_by(Address.id).all()
        last_address = address[-1]
        url = f"/api/address/{last_address.id}"
        client = app.test_client()
        response = client.get(url)

        self.assertEqual(200, response.status_code)
        self.assertEqual(last_address.id, response.json['id'])
        self.assertEqual(last_address.name, response.json['name'])

    def test_get_address_not_exist(self):
        """If address doesnt exist Api should return error message"""
        address_id = 999999999
        client = app.test_client()
        url = f"/api/address/{address_id}"
        message = f"Could not find address with ID: {address_id}."
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_str_id_format(self):
        """If address id have wrong format, Api should return error message"""
        address_id = "one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/address/{address_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_negative_num_id_format(self):
        """If address id have wrong format, Api should return error message"""
        address_id = -1
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/address/{address_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_str_num_id_format(self):
        """If address id have wrong format, Api should return error message"""
        address_id = "1one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/address/{address_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_float_num_id_format(self):
        """If address id have wrong format, Api should return error message"""
        address_id = 1.0
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/address/{address_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_address(self):
        """Api should update address information"""
        address = Address.query.order_by(Address.id).all()
        client = app.test_client()
        last_address = address[-1]
        update_test_data = {'name': 'update_test_address'}
        url = f"/api/address/{last_address.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(201, response.status_code)
        self.assertEqual(last_address.id, response.json['id'])
        self.assertEqual(update_test_data['name'], response.json['name'])

    def test_put_address_not_exist(self):
        """If address doesnt exist Api should return error message"""
        address_id = 999999999
        client = app.test_client()
        url = f"/api/address/{address_id}"
        message = f"Could not find address with ID: {address_id}."
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_str_id_format(self):
        """If address id have wrong format, Api should return error message"""
        address_id = "one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/address/{address_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_negative_num_id_format(self):
        """If address id have wrong format, Api should return error message"""
        address_id = -1
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/address/{address_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_str_num_id_format(self):
        """If address id have wrong format, Api should return error message"""
        address_id = "1one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/address/{address_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_float_num_id_format(self):
        """If address id have wrong format, Api should return error message"""
        address_id = 1.0
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/address/{address_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_big_address_name(self):
        """If address name have wrong format, Api should return error message"""
        address = Address.query.order_by(Address.id).all()
        last_address = address[-1]
        client = app.test_client()
        update_test_data = {'name': 'test_very_big_address_name_test_very_big_address_name_test_very_big_address_name_'
                                    'test_very_big_address_name_test_very_big_address_name_test_very_big_address_name'}
        message = "Exception: 1 validation error for AddressSchema\nname\n  Name length too big! (type=value_error)"
        url = f"/api/address/{last_address.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_address_already_exist(self):
        """If address already exist, Api should return error message"""
        address = Address.query.order_by(Address.id).all()
        client = app.test_client()
        last_address = address[-1]
        update_test_data = {'name': last_address.name}
        message = "Exception: 1 validation error for AddressSchema\n" \
                  "name\n  This address is already in use! (type=value_error)"
        url = f"/api/address/{last_address.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_post_address(self):
        """Api should create new address"""
        test_address = AddressFactory()
        client = app.test_client()
        test_data = {'name': test_address.name}
        url = f"/api/address"
        response = client.post(url, json=test_data)
        self.assertEqual(response.status_code, 201)
        address = Address.query.order_by(Address.id).all()
        last_address = address[-1]
        db.session.delete(last_address)
        db.session.commit()

    def test_post_address_very_long_name(self):
        """Api should create new address"""
        client = app.test_client()
        test_data = {'name': 'test_very_big_address_name_test_very_big_address_name_test_very_big_address_name_'
                             'test_very_big_address_name_test_very_big_address_name_test_very_big_address_name'}
        message = "Exception: 1 validation error for AddressSchema\nname\n  Name length too big! (type=value_error)"
        url = f"/api/address"
        response = client.post(url, json=test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_address_all(self):
        """Api should return all address information"""
        url = f"/api/address"
        client = app.test_client()
        response = client.get(url)
        address = Address.query.order_by(Address.id).all()
        self.assertEqual(len(response.json), len(address))
