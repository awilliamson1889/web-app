from unittest.mock import patch
import unittest

from department_app.rest import Permission, PermissionList
from department_app.tests import PermissionFactory


class TestApiPermission(unittest.TestCase):
    """Test permission api class"""

    @patch('department_app.rest.permission.CRUDPermission.get_permission')
    def test_get_permission(self, mock_get_permission):
        """Api should return information about permission."""
        mock_get_permission.return_value = {'id': 100,
                                            'name': 'Some Permission'}
        response = Permission.get(100)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], 100)
        self.assertEqual(response.json['name'], 'Some Permission')

    @patch('department_app.rest.permission.CRUDPermission.update_permission')
    def test_put_permission(self, mock_update_permission):
        """Api should return information about permission."""
        mock_update_permission.return_value = {'id': 100,
                                               'name': 'Updated Permission'}
        response = Permission.put(100)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['id'], 100)
        self.assertEqual(response.json['name'], 'Updated Permission')

    @patch('department_app.rest.permission.CRUDPermission.create_permission')
    def test_post_permission(self, mock_create_permission):
        """Api should return information about permission."""
        mock_create_permission.return_value = {'id': 100,
                                               'name': 'New Permission'}
        response = PermissionList.post()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['id'], 100)
        self.assertEqual(response.json['name'], 'New Permission')

    @patch('department_app.rest.permission.CRUDPermission.get_all_permission')
    def test_get_all_permission(self, mock_get_all_permission):
        """Api should return information about permissions."""
        mock_get_all_permission.return_value = [
            {
                "permission_id": 1,
                "name": "Some Permission1"
            },
            {
                "permission_id": 2,
                "name": "Some Permission2"
            },
            {
                "permission_id": 3,
                "name": "Some Permission3"
            }]
        response = PermissionList.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 3)
        self.assertEqual(response.json[0]['permission_id'], 1)
        self.assertEqual(response.json[0]['name'], 'Some Permission1')
