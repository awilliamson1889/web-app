from unittest.mock import patch
import unittest

from department_app.rest import Employee, EmployeeList
from department_app.app import create_app

app = create_app()
app.app_context().push()


class TestApiEmployee(unittest.TestCase):
    update_success_msg = "Data successful updated."
    update_fail_msg = "Employee not updated."
    wrong_id_format_msg = "Invalid ID format!"
    not_valid_json_msg = "Employee 12 validation errors for EmployeeSchema\nname\n  Name length too big! " \
                         "(type=value_error)\n" \
                         "surname\n  field required (type=value_error.missing)\ndate_of_birth\n  field required " \
                         "(type=value_error.missing)\nsalary\n  field required (type=value_error.missing)\nemail\n  " \
                         "field required (type=value_error.missing)\nphone\n  field required " \
                         "(type=value_error.missing)\ndate_of_joining\n  field required (type=value_error.missing)\n" \
                         "department\n  field required (type=value_error.missing)\nlocation\n  field required " \
                         "(type=value_error.missing)\nwork_address\n  field required (type=value_error.missing)\n" \
                         "key_skill\n  field required (type=value_error.missing)\npermission\n  field required " \
                         "(type=value_error.missing)"

    wrong_json = {"name_field": "Some Employee1",
                  "manager_field": "Some Manager1",
                  "date_of_creation_field": "1999-12-12"}

    post_valid_data = {"name": "POST Name", "surname": "Surname", "date_of_birth": "1998-01-01", "salary": 500,
                       "email": "email@mail.com", "phone":"444444", "date_of_joining": "2021-05-07", "department": 1,
                       "location": 1, "work_address": 1, "key_skill": 1,
                       "permission": 1}

    put_valid_data = {"name": " PUT Name", "surname": "Surname", "date_of_birth": "1998-01-01", "salary": 500,
                      "email": "email@mail.com", "phone":"444444", "date_of_joining": "2021-05-07", "department": 1,
                      "location": 1, "work_address": 1, "key_skill": 1,
                      "permission": 1}

    post_invalid_data = {"name": "Some Employee1 Some Employee1 Some Employee1 Some Employee1 Some Employee1 "
                                 "Some Employee1 Some Employee1 Some Employee1 Some Employee1 Some Employee1"
                                 "Some Employee1 Some Employee1 Some Employee1 Some Employee1 Some Employee1",
                         "manager": "Some Manager",
                         "date_of_creation": "1999-12-12"}

    valid_test_data = [
        {
            'name': "Some Name", 'surname': "Some Surname", 'date_of_birth': "1999-01-01",
            'salary': 500, 'email': "some@mail.com", 'phone': "3752222222",
            'date_of_joining': "1999-01-01", 'department': "Some Department",
            'location': "Some Location", 'work_address': "Some Work Address", 'key_skill': "Some Skill",
            'permission': "Some Permission", 'department_id': 1, 'employee_id': 1, 'location_id': 1,
            'address_id': 1, 'skill_id': 1, 'permission_id': 1
        },
        {
            'name': "Some Name2", 'surname': "Some Surname2", 'date_of_birth': "1999-01-02",
            'salary': 502, 'email': "some@mail.com2", 'phone': "375333333",
            'date_of_joining': "1999-02-01", 'department': "Some Department2",
            'location': "Some Location2", 'work_address': "Some Work Address2", 'key_skill': "Some Skill2",
            'permission': "Some Permission2", 'department_id': 2, 'employee_id': 2, 'location_id': 2,
            'address_id': 2, 'skill_id': 2, 'permission_id': 2
        }]

    @patch('department_app.rest.employee.CRUDEmployee.get')
    def test_get_employee(self, mock_get_employee):
        """Api should return information about employee."""
        mock_get_employee.return_value = self.valid_test_data[0]
        response = Employee.get(1)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], self.valid_test_data[0]['name'])
        self.assertEqual(response.json['surname'], self.valid_test_data[0]['surname'])
        self.assertEqual(response.json['date_of_birth'], self.valid_test_data[0]['date_of_birth'])
        self.assertEqual(response.json['salary'], self.valid_test_data[0]['salary'])
        self.assertEqual(response.json['email'], self.valid_test_data[0]['email'])
        self.assertEqual(response.json['phone'], self.valid_test_data[0]['phone'])
        self.assertEqual(response.json['date_of_joining'], self.valid_test_data[0]['date_of_joining'])
        self.assertEqual(response.json['department'], self.valid_test_data[0]['department'])
        self.assertEqual(response.json['location'], self.valid_test_data[0]['location'])
        self.assertEqual(response.json['work_address'], self.valid_test_data[0]['work_address'])
        self.assertEqual(response.json['key_skill'], self.valid_test_data[0]['key_skill'])
        self.assertEqual(response.json['permission'], self.valid_test_data[0]['permission'])
        self.assertEqual(response.json['department_id'], self.valid_test_data[0]['department_id'])
        self.assertEqual(response.json['employee_id'], self.valid_test_data[0]['employee_id'])
        self.assertEqual(response.json['location_id'], self.valid_test_data[0]['location_id'])
        self.assertEqual(response.json['address_id'], self.valid_test_data[0]['address_id'])
        self.assertEqual(response.json['skill_id'], self.valid_test_data[0]['skill_id'])
        self.assertEqual(response.json['permission_id'], self.valid_test_data[0]['permission_id'])

    @patch('department_app.rest.employee.abort')
    def test_get_employee_wrong_id_case1(self, mock_abort):
        """Api should return error message if id have wrong format."""
        Employee.get('one')

        mock_abort.assert_called_once_with(404, message="No such employee with ID=one")

    @patch('department_app.rest.employee.abort')
    @patch('department_app.rest.employee.CRUDEmployee.get')
    def test_get_employee_wrong_id_case2(self, mock_get_employee, mock_abort):
        """Api should return error message if id have wrong format."""
        mock_get_employee.return_value = None
        Employee.get(1.0)

        mock_abort.assert_called_once_with(404, message="No such employee with ID=1.0")

    @patch('department_app.rest.employee.abort')
    def test_get_employee_wrong_id_case3(self, mock_abort):
        """Api should return error message if id have wrong format."""
        Employee.get(-1)

        mock_abort.assert_called_once_with(404, message="No such employee with ID=-1")

    @patch('department_app.rest.employee.abort')
    @patch('department_app.rest.employee.CRUDEmployee.get')
    def test_get_employee_not_exist(self, mock_get_employee, mock_abort):
        """Api should return information about employee."""
        mock_get_employee.return_value = None
        Employee.get(1)

        mock_abort.assert_called_once_with(404, message="No such employee with ID=1")

    @patch('department_app.rest.employee.CRUDEmployee.update')
    def test_put_employee_success(self, mock_update):
        """Api should return information about employee."""
        with app.test_request_context(json=self.post_valid_data):
            mock_update.return_value = True
            response = Employee.put(1)

            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json['message'], self.update_success_msg)

    @patch('department_app.rest.employee.abort')
    @patch('department_app.rest.employee.CRUDEmployee.update')
    def test_put_employee_fail(self, mock_update, mock_abort):
        """Api should return information about employee."""
        with app.test_request_context(json=self.post_valid_data):
            mock_update.return_value = False
            Employee.put(1)

            mock_abort.assert_called_once_with(404, message=self.update_fail_msg)

    @patch('department_app.rest.employee.abort')
    def test_put_employee_not_valid(self, mock_abort):
        """Api should return information about employee."""
        with app.test_request_context(json=self.post_invalid_data):
            Employee.put(1)

            mock_abort.assert_called_once_with(404, message=self.not_valid_json_msg)

    @patch('department_app.rest.employee.CRUDEmployee.create')
    def test_post_employee(self, mock_create_employee):
        """Api should return information about employee."""
        with app.test_request_context(json=self.post_valid_data):
            mock_create_employee.return_value = self.post_valid_data
            response = EmployeeList.post()

            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json['name'], self.post_valid_data['name'])
            self.assertEqual(response.json['surname'], self.post_valid_data['surname'])
            self.assertEqual(response.json['date_of_birth'], self.post_valid_data['date_of_birth'])
            self.assertEqual(response.json['salary'], self.post_valid_data['salary'])
            self.assertEqual(response.json['email'], self.post_valid_data['email'])
            self.assertEqual(response.json['phone'], self.post_valid_data['phone'])
            self.assertEqual(response.json['date_of_joining'], self.post_valid_data['date_of_joining'])
            self.assertEqual(response.json['department'], self.post_valid_data['department'])
            self.assertEqual(response.json['location'], self.post_valid_data['location'])
            self.assertEqual(response.json['work_address'], self.post_valid_data['work_address'])
            self.assertEqual(response.json['key_skill'], self.post_valid_data['key_skill'])
            self.assertEqual(response.json['permission'], self.post_valid_data['permission'])

    @patch('department_app.rest.employee.abort')
    def test_post_employee_not_valid(self, mok_abort):
        """Api should return information about employee."""
        with app.test_request_context(json=self.post_invalid_data):
            EmployeeList.post()

            mok_abort.assert_called_once_with(404, message=self.not_valid_json_msg)

    @patch('department_app.rest.employee.CRUDEmployee.get_employee_list')
    def test_get_all_employee(self, mock_get_all_employee):
        """Api should return information about employee."""
        mock_get_all_employee.return_value = self.valid_test_data
        response = EmployeeList.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json[1]['name'], self.valid_test_data[1]['name'])
        self.assertEqual(response.json[1]['surname'], self.valid_test_data[1]['surname'])
        self.assertEqual(response.json[1]['date_of_birth'], self.valid_test_data[1]['date_of_birth'])
        self.assertEqual(response.json[1]['salary'], self.valid_test_data[1]['salary'])
        self.assertEqual(response.json[1]['email'], self.valid_test_data[1]['email'])
        self.assertEqual(response.json[1]['phone'], self.valid_test_data[1]['phone'])
        self.assertEqual(response.json[1]['date_of_joining'], self.valid_test_data[1]['date_of_joining'])
        self.assertEqual(response.json[1]['department'], self.valid_test_data[1]['department'])
        self.assertEqual(response.json[1]['location'], self.valid_test_data[1]['location'])
        self.assertEqual(response.json[1]['work_address'], self.valid_test_data[1]['work_address'])
        self.assertEqual(response.json[1]['key_skill'], self.valid_test_data[1]['key_skill'])
        self.assertEqual(response.json[1]['permission'], self.valid_test_data[1]['permission'])
        self.assertEqual(response.json[1]['department_id'], self.valid_test_data[1]['department_id'])
        self.assertEqual(response.json[1]['employee_id'], self.valid_test_data[1]['employee_id'])
        self.assertEqual(response.json[1]['location_id'], self.valid_test_data[1]['location_id'])
        self.assertEqual(response.json[1]['address_id'], self.valid_test_data[1]['address_id'])
        self.assertEqual(response.json[1]['skill_id'], self.valid_test_data[1]['skill_id'])
        self.assertEqual(response.json[1]['permission_id'], self.valid_test_data[1]['permission_id'])

    @patch('department_app.rest.employee.CRUDEmployee.get_employee_list')
    def test_get_all_employee_empty(self, mock_get_all_employee):
        """Api should return information about employee."""
        mock_get_all_employee.return_value = []
        response = EmployeeList.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 0)
