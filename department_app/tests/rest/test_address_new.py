from unittest.mock import patch
import unittest

from department_app.rest import Address, AddressList
from department_app.tests import AddressFactory


class TestApiAddress(unittest.TestCase):
    """Test address api class"""

    @patch('department_app.rest.address.CRUDAddress.get')
    def test_get_address(self, mock_get_address):
        """Api should return information about address."""
        mock_get_address.return_value = {'id': 100,
                                         'name': 'Some Address'}
        response = Address.get(100)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], 100)
        self.assertEqual(response.json['name'], 'Some Address')

    @patch('department_app.rest.address.Address.check_exist')
    @patch('department_app.rest.address.Address.get_json')
    @patch('department_app.rest.address.CRUDAddress.update')
    def test_put_address(self, mock_update_address, mok_get_json, mock_check_exist):
        """Api should return information about address."""
        mok_get_json.return_value = {'name': 'Updated Address'}
        mock_check_exist.return_value = True
        mock_update_address.return_value = {'id': 100,
                                            'name': 'Updated Address'}
        response = Address.put(100)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['id'], 100)
        self.assertEqual(response.json['name'], 'Updated Address')

    @patch('department_app.rest.address.Address.get_json')
    @patch('department_app.rest.address.CRUDAddress.create')
    def test_post_address(self, mock_create_address, mok_get_json):
        """Api should return information about address."""
        mok_get_json.return_value = {'name': 'New Address'}
        mock_create_address.return_value = {'id': 100,
                                            'name': 'New Address'}
        response = AddressList.post()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['id'], 100)
        self.assertEqual(response.json['name'], 'New Address')

    @patch('department_app.rest.address.CRUDAddress.get_address_list')
    def test_get_all_address(self, mock_get_all_address):
        """Api should return information about address."""
        mock_get_all_address.return_value = [
            {
                "address_id": 1,
                "name": "Some Address1"
            },
            {
                "address_id": 2,
                "name": "Some Address2"
            },
            {
                "address_id": 3,
                "name": "Some Address3"
            }]
        response = AddressList.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 3)
        self.assertEqual(response.json[0]['address_id'], 1)
        self.assertEqual(response.json[0]['name'], 'Some Address1')
