from flask import copy_current_request_context
import requests
from unittest.mock import patch
import unittest

from department_app.rest import Address, AddressList
from department_app.app import create_app

app = create_app()
app.app_context().push()


class TestApiAddress(unittest.TestCase):
    """Test address api class"""
    update_success_msg = "Data successful updated."
    update_fail_msg = "Address not updated."
    wrong_id_format_msg = "Invalid ID format!"
    wrong_json_msg = "1 validation error for AddressSchema\nname\n  field required (type=value_error.missing)"
    not_valid_json_msg = "1 validation error for AddressSchema\nname\n  Name length too big! (type=value_error)"

    wrong_json = {"name_field": "Some Address1"}

    post_valid_data = {"name": "POST ADDRESS"}
    put_valid_data = {"name": "PUT ADDRESS"}
    post_invalid_data = {"name": "Some Address1 Some Address1 Some Address1 Some Address1 Some Address1 Some Address1"
                                 "Some Address1 Some Address1 Some Address1 Some Address1 Some Address1 Some Address1"
                                 "Some Address1 Some Address1 Some Address1 Some Address1 Some Address1 Some Address1"}

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
                "name": "Some Address3"}]

    @patch('department_app.rest.address.CRUDAddress.get')
    def test_get_address(self, mock_get_address):
        """Api should return information about address."""
        mock_get_address.return_value = self.valid_test_data[0]
        response = Address.get(1)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], self.valid_test_data[0]['id'])
        self.assertEqual(response.json['name'], self.valid_test_data[0]['name'])

    @patch('department_app.rest.address.abort')
    def test_get_address_wrong_id_case1(self, mock_abort):
        """Api should return information about address."""
        Address.get('one')

        mock_abort.assert_called_once_with(404, message="No such address with ID=one")

    @patch('department_app.rest.address.abort')
    def test_get_address_wrong_id_case2(self, mock_abort):
        """Api should return information about address."""
        Address.get(-1)

        mock_abort.assert_called_once_with(404, message="No such address with ID=-1")

    @patch('department_app.rest.address.abort')
    @patch('department_app.rest.address.CRUDAddress.get')
    def test_get_address_wrong_id_case3(self, mock_get_address, mock_abort):
        """Api should return information about address."""
        mock_get_address.return_value = None
        Address.get(1.0)

        mock_abort.assert_called_once_with(404, message="No such address with ID=1.0")

    @patch('department_app.rest.address.abort')
    @patch('department_app.rest.address.CRUDAddress.get')
    def test_get_address_not_exist(self, mock_get_address, mock_abort):
        """Api should return information about address."""
        mock_get_address.return_value = None
        Address.get(1)

        mock_abort.assert_called_once_with(404, message="No such address with ID=1")

    @patch('department_app.rest.address.CRUDAddress.update')
    def test_put_address_success(self,  mock_update):
        """Api should return information about address."""
        with app.test_request_context(json=self.post_valid_data):

            mock_update.return_value = True
            response = Address.put(1)

            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json['message'], self.update_success_msg)

    @patch('department_app.rest.address.abort')
    @patch('department_app.rest.address.CRUDAddress.update')
    def test_put_address_fail(self, mock_update, mock_abort):
        """Api should return information about address."""
        with app.test_request_context(json=self.post_valid_data):
            mock_update.return_value = False
            Address.put(1)

            mock_abort.assert_called_once_with(404, message=self.update_fail_msg)

    @patch('department_app.rest.address.abort')
    def test_put_address_not_valid(self, mock_abort):
        """Api should return information about address."""
        with app.test_request_context(json=self.post_invalid_data):
            Address.put(1)

            mock_abort.assert_called_once_with(404, message=self.not_valid_json_msg)

    @patch('department_app.rest.address.abort')
    def test_put_address_wrong_json(self, mock_abort):
        """Api should return information about address."""
        with app.test_request_context(json=self.wrong_json):
            Address.put(1)

            mock_abort.assert_called_once_with(404, message=self.wrong_json_msg)

    @patch('department_app.rest.address.CRUDAddress.create')
    def test_post_address(self, mock_create_address):
        """Api should return information about address."""
        with app.test_request_context(json=self.post_valid_data):
            mock_create_address.return_value = {'id': 1,
                                                'name': self.post_valid_data['name']}
            response = AddressList.post()

            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json['id'], 1)
            self.assertEqual(response.json['name'], self.post_valid_data['name'])

    @patch('department_app.rest.address.abort')
    def test_post_address_not_valid(self, mok_abort):
        """Api should return information about address."""
        with app.test_request_context(json=self.post_invalid_data):
            AddressList.post()

            mok_abort.assert_called_once_with(404, message=self.not_valid_json_msg)

    @patch('department_app.rest.address.abort')
    def test_post_address_wrong_json(self, mock_abort):
        """Api should return information about address."""
        with app.test_request_context(json=self.wrong_json):
            AddressList.post()

            mock_abort.assert_called_once_with(404, message=self.wrong_json_msg)

    @patch('department_app.rest.address.CRUDAddress.get_address_list')
    def test_get_all_address(self, mock_get_all_address):
        """Api should return information about address."""
        mock_get_all_address.return_value = self.valid_test_data
        response = AddressList.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), len(self.valid_test_data))
        self.assertEqual(response.json[0]['id'], self.valid_test_data[0]['id'])
        self.assertEqual(response.json[0]['name'], self.valid_test_data[0]['name'])

    @patch('department_app.rest.address.CRUDAddress.get_address_list')
    def test_get_all_address_empty(self, mock_get_all_address):
        """Api should return information about address."""
        mock_get_all_address.return_value = []
        response = AddressList.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 0)
