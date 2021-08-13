from unittest.mock import patch
import unittest

from department_app.rest import Location, LocationList
from department_app.tests import LocationFactory


class TestApiLocation(unittest.TestCase):
    """Test location api class"""

    @patch('department_app.rest.location.CRUDLocation.get_location')
    def test_get_location(self, mock_get_location):
        """Api should return information about location."""
        mock_get_location.return_value = {'id': 100,
                                          'name': 'Some Location'}
        response = Location.get(100)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], 100)
        self.assertEqual(response.json['name'], 'Some Location')

    @patch('department_app.rest.location.CRUDLocation.update_location')
    def test_put_location(self, mock_update_location):
        """Api should return information about location."""
        mock_update_location.return_value = {'id': 100,
                                             'name': 'Updated Location'}
        response = Location.put(100)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['id'], 100)
        self.assertEqual(response.json['name'], 'Updated Location')

    @patch('department_app.rest.location.CRUDLocation.create_location')
    def test_post_location(self, mock_create_location):
        """Api should return information about location."""
        mock_create_location.return_value = {'id': 100,
                                             'name': 'New Location'}
        response = LocationList.post()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['id'], 100)
        self.assertEqual(response.json['name'], 'New Location')

    @patch('department_app.rest.location.CRUDLocation.get_all_location')
    def test_get_all_location(self, mock_get_all_location):
        """Api should return information about locations."""
        mock_get_all_location.return_value = [
            {
                "location_id": 1,
                "name": "Some Location1"
            },
            {
                "location_id": 2,
                "name": "Some Location2"
            },
            {
                "location_id": 3,
                "name": "Some Location3"
            }]
        response = LocationList.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 3)
        self.assertEqual(response.json[0]['location_id'], 1)
        self.assertEqual(response.json[0]['name'], 'Some Location1')
