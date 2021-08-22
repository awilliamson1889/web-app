from unittest.mock import patch
import unittest

from department_app.rest import Permission, PermissionList
from department_app.app import create_app

app = create_app()
app.app_context().push()


class TestApiPermission(unittest.TestCase):
    """Test permission api class"""
    update_success_msg = "Data successful updated."
    update_fail_msg = "Permission not updated."
    wrong_id_format_msg = "Invalid ID format!"
    wrong_json_msg = "Wrong JSON fields names."
    not_valid_json_msg = "JSON is not valid."

    wrong_json = {"name_field": "Some Permission1"}

    post_valid_data = {"name": "POST PERMISSION"}
    put_valid_data = {"name": "PUT PERMISSION"}
    post_invalid_data = {"name": "Some Permission1 Some Permission1 Some Permission1 Some Permission1 Some Permission1"
                                 "Some Permission1 Some Permission1 Some Permission1 Some Permission1 Some Permission1"
                                 "Some Permission1 Some Permission1 Some Permission1 Some Permission1 Some Permission1"
                                 "Some Permission1 Some Permission1 Some Permission1 Some Permission1 Some Permission1"}

    valid_test_data = [
            {
                "id": 1,
                "name": "Some Permission1"
            },
            {
                "id": 2,
                "name": "Some Permission2"
            },
            {
                "id": 3,
                "name": "Some Permission3"}]

    @patch('department_app.rest.permission.CRUDPermission.get')
    def test_get_permission(self, mock_get_permission):
        """Api should return information about permission."""
        mock_get_permission.return_value = self.valid_test_data[0]
        response = Permission.get(1)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], self.valid_test_data[0]['id'])
        self.assertEqual(response.json['name'], self.valid_test_data[0]['name'])

    @patch('department_app.rest.permission.abort')
    def test_get_permission_wrong_id_case1(self, mock_abort):
        """Api should return information about permission."""
        Permission.get('one')

        mock_abort.assert_called_once_with(404, message=self.wrong_id_format_msg)

    @patch('department_app.rest.permission.abort')
    def test_get_permission_wrong_id_case2(self, mock_abort):
        """Api should return information about permission."""
        Permission.get(-1)

        mock_abort.assert_called_once_with(404, message=self.wrong_id_format_msg)

    @patch('department_app.rest.permission.abort')
    def test_get_permission_wrong_id_case3(self, mock_abort):
        """Api should return information about permission."""
        Permission.get(1.0)

        mock_abort.assert_called_once_with(404, message=self.wrong_id_format_msg)

    @patch('department_app.rest.permission.abort')
    @patch('department_app.rest.permission.CRUDPermission.get')
    def test_get_permission_not_exist(self, mock_get_permission, mock_abort):
        """Api should return information about permission."""
        mock_get_permission.return_value = None
        Permission.get(1)

        mock_abort.assert_called_once_with(404, message="No such permission with ID=1")

    @patch('department_app.rest.permission.CRUDPermission.update')
    @patch('department_app.rest.permission.Permission.get_json')
    def test_put_permission_success(self, mok_get_json, mock_update):
        """Api should return information about permission."""
        mok_get_json.return_value = self.put_valid_data
        mock_update.return_value = True
        response = Permission.put(1)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], self.update_success_msg)

    @patch('department_app.rest.permission.abort')
    @patch('department_app.rest.permission.CRUDPermission.update')
    @patch('department_app.rest.permission.Permission.get_json')
    def test_put_permission_fail(self, mok_get_json, mock_update, mock_abort):
        """Api should return information about permission."""
        mok_get_json.return_value = self.put_valid_data
        mock_update.return_value = False
        Permission.put(1)

        mock_abort.assert_called_once_with(404, message=self.update_fail_msg)

    @patch('department_app.rest.permission.abort')
    @patch('department_app.rest.permission.Permission.get_json')
    def test_put_permission_not_valid(self, mok_get_json, mock_abort):
        """Api should return information about permission."""
        mok_get_json.return_value = self.post_invalid_data
        Permission.put(1)

        mock_abort.assert_called_once_with(404, message=self.not_valid_json_msg)

    @patch('department_app.rest.permission.abort')
    @patch('department_app.rest.permission.Permission.get_json')
    def test_put_permission_wrong_json(self, mok_get_json, mock_abort):
        """Api should return information about permission."""
        mok_get_json.return_value = False
        Permission.put(1)

        mock_abort.assert_called_once_with(404, message=self.wrong_json_msg)

    @patch('department_app.rest.permission.Permission.get_json')
    @patch('department_app.rest.permission.CRUDPermission.create')
    def test_post_permission(self, mock_create_permission, mok_get_json):
        """Api should return information about permission."""
        mok_get_json.return_value = self.post_valid_data
        mock_create_permission.return_value = {'id': 1,
                                            'name': self.post_valid_data['name']}
        response = PermissionList.post()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['id'], 1)
        self.assertEqual(response.json['name'], self.post_valid_data['name'])

    @patch('department_app.rest.permission.abort')
    @patch('department_app.rest.permission.Permission.get_json')
    def test_post_permission_not_valid(self, mok_get_json, mok_abort):
        """Api should return information about permission."""
        mok_get_json.return_value = self.post_invalid_data

        PermissionList.post()

        mok_abort.assert_called_once_with(404, message=self.not_valid_json_msg)

    @patch('department_app.rest.permission.abort')
    @patch('department_app.rest.permission.Permission.get_json')
    def test_post_permission_wrong_json(self, mok_get_json, mock_abort):
        """Api should return information about permission."""
        mok_get_json.return_value = False

        PermissionList.post()

        mock_abort.assert_called_once_with(404, message=self.wrong_json_msg)

    @patch('department_app.rest.permission.CRUDPermission.get_permission_list')
    def test_get_all_permission(self, mock_get_all_permission):
        """Api should return information about permission."""
        mock_get_all_permission.return_value = self.valid_test_data
        response = PermissionList.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), len(self.valid_test_data))
        self.assertEqual(response.json[0]['id'], self.valid_test_data[0]['id'])
        self.assertEqual(response.json[0]['name'], self.valid_test_data[0]['name'])

    @patch('department_app.rest.permission.CRUDPermission.get_permission_list')
    def test_get_all_permission_empty(self, mock_get_all_permission):
        """Api should return information about permission."""
        mock_get_all_permission.return_value = []
        response = PermissionList.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 0)
