from unittest.mock import patch
import unittest

from department_app.rest import Address, AddressList
from department_app.app import create_app

app = create_app()
app.app_context().push()


class TestApiAddress(unittest.TestCase):
    """Test address api class"""
    wrong_id_format_msg = "Invalid ID format!"

    post_valid_data = {"name": "POST ADDRESS"}

    valid_test_data = [
            {
                "id": 1,
                "name": "Some Address1"
            },
            {
                "id": 2,
                "name": "Some Address2"
            },
            {
                "id": 3,
                "name": "Some Address3"
            }]

    @patch('department_app.rest.address.CRUDAddress.get')
    def test_get_address(self, mock_get_address):
        """Api should return information about address."""
        mock_get_address.return_value = self.valid_test_data[0]
        response = Address.get(1)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], self.valid_test_data[0]['id'])
        self.assertEqual(response.json['name'], self.valid_test_data[0]['name'])

    @patch('department_app.rest.address.Address.get_json')
    @patch('department_app.rest.address.CRUDAddress.update')
    def test_put_address_success(self, mock_update_address, mok_get_json):
        """Api should return information about address."""
        mok_get_json.return_value = self.valid_test_data[1]
        mock_update_address.return_value = True
        response = Address.put(1)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Data successful updated.')

    @patch('department_app.rest.address.Address.get_json')
    @patch('department_app.rest.address.CRUDAddress.create')
    def test_post_address(self, mock_create_address, mok_get_json):
        """Api should return information about address."""
        mok_get_json.return_value = self.post_valid_data
        mock_create_address.return_value = {'id': 1,
                                            'name': self.post_valid_data['name']}
        response = AddressList.post()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['id'], 1)
        self.assertEqual(response.json['name'], self.post_valid_data['name'])

    @patch('department_app.rest.address.CRUDAddress.get_address_list')
    def test_get_all_address(self, mock_get_all_address):
        """Api should return information about address."""
        mock_get_all_address.return_value = self.valid_test_data
        response = AddressList.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), len(self.valid_test_data))
        self.assertEqual(response.json[0]['id'], self.valid_test_data[0]['id'])
        self.assertEqual(response.json[0]['name'], self.valid_test_data[0]['name'])
