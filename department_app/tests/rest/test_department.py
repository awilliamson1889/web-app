from unittest.mock import patch
import unittest

from department_app.rest import Department, DepartmentList
from department_app.app import create_app

app = create_app()
app.app_context().push()


class TestApiDepartment(unittest.TestCase):
    update_success_msg = "Data successful updated."
    update_fail_msg = "Department not updated."
    wrong_id_format_msg = "Invalid ID format!"
    wrong_json_msg = "Wrong JSON fields names."
    not_valid_json_msg = "JSON is not valid."

    wrong_json = {"name_field": "Some Department1",
                  "manager_field": "Some Manager1",
                  "date_of_creation_field": "1999-12-12"}

    post_valid_data = {"name": "POST LOCATION",
                       "manager": "Some Manager",
                       "date_of_creation": "1999-12-12"}

    put_valid_data = {"name": "PUT LOCATION",
                      "manager": "Some Manager",
                      "date_of_creation": "1999-12-12"}

    post_invalid_data = {"name": "Some Department1 Some Department1 Some Department1 Some Department1 Some Department1 "
                                 "Some Department1 Some Department1 Some Department1 Some Department1 Some Department1"
                                 "Some Department1 Some Department1 Some Department1 Some Department1 Some Department1",
                         "manager": "Some Manager",
                         "date_of_creation": "1999-12-12"}

    valid_test_data = [
        {
            'name': "Some Department1",
            'manager': "Some Manager1",
            'date_of_creation': "2021-12-12",
            'employees': 15,
            'department_avg_salary': 2400,
            'department_id': 1
        },
        {
            'name': "Some Department2",
            'manager': "Some Manager2",
            'date_of_creation': "2021-12-12",
            'employees': 25,
            'department_avg_salary': 2880,
            'department_id': 2
        },
        {
            'name': "Some Department3",
            'manager': "Some Manager3",
            'date_of_creation': "2021-12-12",
            'employees': 44,
            'department_avg_salary': 5500,
            'department_id': 3}]

    @patch('department_app.rest.department.CRUDDepartment.get')
    def test_get_department(self, mock_get_department):
        """Api should return information about department."""
        mock_get_department.return_value = self.valid_test_data[0]
        response = Department.get(1)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['department_id'], self.valid_test_data[0]['department_id'])
        self.assertEqual(response.json['manager'], self.valid_test_data[0]['manager'])
        self.assertEqual(response.json['date_of_creation'], self.valid_test_data[0]['date_of_creation'])
        self.assertEqual(response.json['employees'], self.valid_test_data[0]['employees'])
        self.assertEqual(response.json['department_avg_salary'], self.valid_test_data[0]['department_avg_salary'])
        self.assertEqual(response.json['name'], self.valid_test_data[0]['name'])

    @patch('department_app.rest.department.abort')
    def test_get_department_wrong_id_case1(self, mock_abort):
        """Api should return error message if id have wrong format."""
        Department.get('one')

        mock_abort.assert_called_once_with(404, message=self.wrong_id_format_msg)

    @patch('department_app.rest.department.abort')
    def test_get_department_wrong_id_case2(self, mock_abort):
        """Api should return error message if id have wrong format."""
        Department.get(1.0)

        mock_abort.assert_called_once_with(404, message=self.wrong_id_format_msg)

    @patch('department_app.rest.department.abort')
    def test_get_department_wrong_id_case3(self, mock_abort):
        """Api should return error message if id have wrong format."""
        Department.get(-1)

        mock_abort.assert_called_once_with(404, message=self.wrong_id_format_msg)

    @patch('department_app.rest.department.abort')
    @patch('department_app.rest.department.CRUDDepartment.get')
    def test_get_department_not_exist(self, mock_get_department, mock_abort):
        """Api should return information about department."""
        mock_get_department.return_value = None
        Department.get(1)

        mock_abort.assert_called_once_with(404, message="No such department with ID=1")

    @patch('department_app.rest.department.CRUDDepartment.update')
    @patch('department_app.rest.department.Department.get_json')
    def test_put_department_success(self, mok_get_json, mock_update):
        """Api should return information about department."""
        mok_get_json.return_value = self.put_valid_data
        mock_update.return_value = True
        response = Department.put(1)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], self.update_success_msg)

    @patch('department_app.rest.department.abort')
    @patch('department_app.rest.department.CRUDDepartment.update')
    @patch('department_app.rest.department.Department.get_json')
    def test_put_department_fail(self, mok_get_json, mock_update, mock_abort):
        """Api should return information about department."""
        mok_get_json.return_value = self.put_valid_data
        mock_update.return_value = False
        Department.put(1)

        mock_abort.assert_called_once_with(404, message=self.update_fail_msg)

    @patch('department_app.rest.department.abort')
    @patch('department_app.rest.department.Department.get_json')
    def test_put_department_not_valid(self, mok_get_json, mock_abort):
        """Api should return information about department."""
        mok_get_json.return_value = self.post_invalid_data
        Department.put(1)

        mock_abort.assert_called_once_with(404, message=self.not_valid_json_msg)

    @patch('department_app.rest.department.abort')
    @patch('department_app.rest.department.Department.get_json')
    def test_put_department_wrong_json(self, mok_get_json, mock_abort):
        """Api should return information about department."""
        mok_get_json.return_value = False
        Department.put(1)

        mock_abort.assert_called_once_with(404, message=self.wrong_json_msg)

    @patch('department_app.rest.department.Department.get_json')
    @patch('department_app.rest.department.CRUDDepartment.create')
    def test_post_department(self, mock_create_department, mok_get_json):
        """Api should return information about department."""
        mok_get_json.return_value = self.post_valid_data
        mock_create_department.return_value = self.post_valid_data
        response = DepartmentList.post()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], self.post_valid_data['name'])
        self.assertEqual(response.json['manager'], self.post_valid_data['manager'])
        self.assertEqual(response.json['date_of_creation'], self.post_valid_data['date_of_creation'])

    @patch('department_app.rest.department.abort')
    @patch('department_app.rest.department.Department.get_json')
    def test_post_department_not_valid(self, mok_get_json, mok_abort):
        """Api should return information about department."""
        mok_get_json.return_value = self.post_invalid_data

        DepartmentList.post()

        mok_abort.assert_called_once_with(404, message=self.not_valid_json_msg)

    @patch('department_app.rest.department.abort')
    @patch('department_app.rest.department.Department.get_json')
    def test_post_department_wrong_json(self, mok_get_json, mock_abort):
        """Api should return information about department."""
        mok_get_json.return_value = False

        DepartmentList.post()

        mock_abort.assert_called_once_with(404, message=self.wrong_json_msg)

    @patch('department_app.rest.department.CRUDDepartment.get_department_list')
    def test_get_all_department(self, mock_get_all_department):
        """Api should return information about department."""
        mock_get_all_department.return_value = self.valid_test_data
        response = DepartmentList.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), len(self.valid_test_data))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json[1]['department_id'], self.valid_test_data[1]['department_id'])
        self.assertEqual(response.json[1]['manager'], self.valid_test_data[1]['manager'])
        self.assertEqual(response.json[1]['date_of_creation'], self.valid_test_data[1]['date_of_creation'])
        self.assertEqual(response.json[1]['employees'], self.valid_test_data[1]['employees'])
        self.assertEqual(response.json[1]['department_avg_salary'], self.valid_test_data[1]['department_avg_salary'])
        self.assertEqual(response.json[1]['name'], self.valid_test_data[1]['name'])

    @patch('department_app.rest.department.CRUDDepartment.get_department_list')
    def test_get_all_department_empty(self, mock_get_all_department):
        """Api should return information about department."""
        mock_get_all_department.return_value = []
        response = DepartmentList.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 0)
