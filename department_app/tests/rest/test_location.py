from unittest.mock import patch
import unittest

from department_app.rest import Location, LocationList
from department_app.app import create_app

app = create_app()
app.app_context().push()


class TestApiLocation(unittest.TestCase):
    update_success_msg = "Data successful updated."
    update_fail_msg = "Location not updated."
    wrong_id_format_msg = "Invalid ID format!"
    wrong_json_msg = "Wrong JSON fields names."
    not_valid_json_msg = "JSON is not valid."

    wrong_json = {"name_field": "Some Location1"}

    post_valid_data = {"name": "POST LOCATION"}
    put_valid_data = {"name": "PUT LOCATION"}
    post_invalid_data = {"name": "Some Location1 Some Location1 Some Location1 Some Location1 Some Location1 "
                                 "Some Location1 Some Location1 Some Location1 Some Location1 Some Location1"
                                 "Some Location1 Some Location1 Some Location1 Some Location1 Some Location1"}

    valid_test_data = [
            {
                "id": 1,
                "name": "Some Location1"
            },
            {
                "id": 2,
                "name": "Some Location2"
            },
            {
                "id": 3,
                "name": "Some Location3"}]

    @patch('department_app.rest.location.CRUDLocation.get')
    def test_get_location(self, mock_get_location):
        """Api should return information about location."""
        mock_get_location.return_value = self.valid_test_data[0]
        response = Location.get(1)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], self.valid_test_data[0]['id'])
        self.assertEqual(response.json['name'], self.valid_test_data[0]['name'])

    @patch('department_app.rest.location.abort')
    def test_get_location_wrong_id_case1(self, mock_abort):
        """Api should return error message if id have wrong format."""
        Location.get('one')

        mock_abort.assert_called_once_with(404, message=self.wrong_id_format_msg)

    @patch('department_app.rest.location.abort')
    def test_get_location_wrong_id_case2(self, mock_abort):
        """Api should return error message if id have wrong format."""
        Location.get(1.0)

        mock_abort.assert_called_once_with(404, message=self.wrong_id_format_msg)

    @patch('department_app.rest.location.abort')
    def test_get_location_wrong_id_case3(self, mock_abort):
        """Api should return error message if id have wrong format."""
        Location.get(-1)

        mock_abort.assert_called_once_with(404, message=self.wrong_id_format_msg)

    @patch('department_app.rest.location.abort')
    @patch('department_app.rest.location.CRUDLocation.get')
    def test_get_location_not_exist(self, mock_get_location, mock_abort):
        """Api should return information about location."""
        mock_get_location.return_value = None
        Location.get(1)

        mock_abort.assert_called_once_with(404, message="No such location with ID=1")

    @patch('department_app.rest.location.CRUDLocation.update')
    @patch('department_app.rest.location.Location.get_json')
    def test_put_location_success(self, mok_get_json, mock_update):
        """Api should return information about location."""
        mok_get_json.return_value = self.put_valid_data
        mock_update.return_value = True
        response = Location.put(1)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], self.update_success_msg)

    @patch('department_app.rest.location.abort')
    @patch('department_app.rest.location.CRUDLocation.update')
    @patch('department_app.rest.location.Location.get_json')
    def test_put_location_fail(self, mok_get_json, mock_update, mock_abort):
        """Api should return information about location."""
        mok_get_json.return_value = self.put_valid_data
        mock_update.return_value = False
        Location.put(1)

        mock_abort.assert_called_once_with(404, message=self.update_fail_msg)

    @patch('department_app.rest.location.abort')
    @patch('department_app.rest.location.Location.get_json')
    def test_put_location_not_valid(self, mok_get_json, mock_abort):
        """Api should return information about location."""
        mok_get_json.return_value = self.post_invalid_data
        Location.put(1)

        mock_abort.assert_called_once_with(404, message=self.not_valid_json_msg)

    @patch('department_app.rest.location.abort')
    @patch('department_app.rest.location.Location.get_json')
    def test_put_location_wrong_json(self, mok_get_json, mock_abort):
        """Api should return information about location."""
        mok_get_json.return_value = False
        Location.put(1)

        mock_abort.assert_called_once_with(404, message=self.wrong_json_msg)

    @patch('department_app.rest.location.Location.get_json')
    @patch('department_app.rest.location.CRUDLocation.create')
    def test_post_location(self, mock_create_location, mok_get_json):
        """Api should return information about location."""
        mok_get_json.return_value = self.post_valid_data
        mock_create_location.return_value = {'id': 1,
                                            'name': self.post_valid_data['name']}
        response = LocationList.post()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['id'], 1)
        self.assertEqual(response.json['name'], self.post_valid_data['name'])

    @patch('department_app.rest.location.abort')
    @patch('department_app.rest.location.Location.get_json')
    def test_post_location_not_valid(self, mok_get_json, mok_abort):
        """Api should return information about location."""
        mok_get_json.return_value = self.post_invalid_data

        LocationList.post()

        mok_abort.assert_called_once_with(404, message=self.not_valid_json_msg)

    @patch('department_app.rest.location.abort')
    @patch('department_app.rest.location.Location.get_json')
    def test_post_location_wrong_json(self, mok_get_json, mock_abort):
        """Api should return information about location."""
        mok_get_json.return_value = False

        LocationList.post()

        mock_abort.assert_called_once_with(404, message=self.wrong_json_msg)

    @patch('department_app.rest.location.CRUDLocation.get_location_list')
    def test_get_all_location(self, mock_get_all_location):
        """Api should return information about location."""
        mock_get_all_location.return_value = self.valid_test_data
        response = LocationList.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), len(self.valid_test_data))
        self.assertEqual(response.json[0]['id'], self.valid_test_data[0]['id'])
        self.assertEqual(response.json[0]['name'], self.valid_test_data[0]['name'])

    @patch('department_app.rest.location.CRUDLocation.get_location_list')
    def test_get_all_location_empty(self, mock_get_all_location):
        """Api should return information about location."""
        mock_get_all_location.return_value = []
        response = LocationList.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 0)

        