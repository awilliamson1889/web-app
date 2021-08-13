from unittest.mock import patch
import unittest

from department_app.rest import Employee, EmployeeList
from department_app.tests import EmployeeFactory


class TestApiEmployee(unittest.TestCase):
    """Test employee api class"""

    @patch('department_app.rest.employee.CRUDEmployee.get_employee')
    def test_get_employee(self, mock_get_employee):
        """Api should return information about employee."""
        mock_get_employee.return_value = {'name': 'Some Name',
                                          'surname': 'Some Surname',
                                          'date_of_birth': '1999-01-01',
                                          'salary': 444.44,
                                          'email': 'some.email@gmail.com',
                                          'phone': '375292002400',
                                          'date_of_joining': '2021-07-12',
                                          'department': 'Some Department',
                                          'location': 'Some Location',
                                          'work_address': 'Some Work Address',
                                          'permission': 'Some Permission',
                                          'department_id': 1,
                                          'employee_id': 100,
                                          'location_id': 1,
                                          'address_id': 1,
                                          'skill_id': 1,
                                          'permission_id': 1}
        response = Employee.get(100)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Some Name')
        self.assertEqual(response.json['surname'], 'Some Surname')
        self.assertEqual(response.json['date_of_birth'], '1999-01-01')
        self.assertEqual(response.json['salary'], 444.44)
        self.assertEqual(response.json['email'], 'some.email@gmail.com')
        self.assertEqual(response.json['phone'], '375292002400')
        self.assertEqual(response.json['date_of_joining'], '2021-07-12')
        self.assertEqual(response.json['department'], 'Some Department')
        self.assertEqual(response.json['location'], 'Some Location')
        self.assertEqual(response.json['work_address'], 'Some Work Address')
        self.assertEqual(response.json['permission'], 'Some Permission')
        self.assertEqual(response.json['department_id'], 1)
        self.assertEqual(response.json['employee_id'], 100)
        self.assertEqual(response.json['skill_id'], 1)
        self.assertEqual(response.json['location_id'], 1)
        self.assertEqual(response.json['address_id'], 1)
        self.assertEqual(response.json['permission_id'], 1)

    @patch('department_app.rest.employee.CRUDEmployee.update_employee')
    def test_put_employee(self, mock_update_employee):
        """Api should return information about employee."""
        mock_update_employee.return_value = {'name': 'Updated Name',
                                             'surname': 'Updated Surname',
                                             'date_of_birth': '1999-01-01',
                                             'salary': 777.77,
                                             'email': 'employee.email@updaate.com',
                                             'phone': '375298870007',
                                             'date_of_joining': '2021-08-01',
                                             'department': 1,
                                             'location': 1,
                                             'work_address': 1,
                                             'key_skill': 1,
                                             'permission': 1,
                                             'id': 100}
        response = Employee.put(100)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], 'Updated Name')
        self.assertEqual(response.json['surname'], 'Updated Surname')
        self.assertEqual(response.json['date_of_birth'], '1999-01-01')
        self.assertEqual(response.json['salary'], 777.77)
        self.assertEqual(response.json['email'], 'employee.email@updaate.com')
        self.assertEqual(response.json['phone'], '375298870007')
        self.assertEqual(response.json['date_of_joining'], '2021-08-01')
        self.assertEqual(response.json['work_address'], 1)
        self.assertEqual(response.json['key_skill'], 1)
        self.assertEqual(response.json['permission'], 1)
        self.assertEqual(response.json['id'], 100)

    @patch('department_app.rest.employee.CRUDEmployee.create_employee')
    def test_post_employee(self, mock_create_employee):
        """Api should return information about employee."""
        mock_create_employee.return_value = {'name': 'New Name',
                                             'surname': 'New Surname',
                                             'date_of_birth': '1999-01-01',
                                             'salary': 777.77,
                                             'email': 'employee.email@new.com',
                                             'phone': '375298870007',
                                             'date_of_joining': '2021-08-01',
                                             'department': 1,
                                             'location': 1,
                                             'work_address': 1,
                                             'key_skill': 1,
                                             'permission': 1}
        response = EmployeeList.post()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], 'New Name')
        self.assertEqual(response.json['surname'], 'New Surname')
        self.assertEqual(response.json['date_of_birth'], '1999-01-01')
        self.assertEqual(response.json['salary'], 777.77)
        self.assertEqual(response.json['email'], 'employee.email@new.com')
        self.assertEqual(response.json['phone'], '375298870007')
        self.assertEqual(response.json['date_of_joining'], '2021-08-01')
        self.assertEqual(response.json['work_address'], 1)
        self.assertEqual(response.json['key_skill'], 1)
        self.assertEqual(response.json['permission'], 1)

    @patch('department_app.rest.employee.CRUDEmployee.get_all_employee')
    def test_get_all_employee(self, mock_get_all_employee):
        """Api should return information about employee."""
        mock_get_all_employee.return_value = [
            {'name': 'Some Name',
             'surname': 'Some Surname',
             'date_of_birth': '1999-01-01',
             'salary': 444.44,
             'email': 'some.email@gmail.com',
             'phone': '375292002400',
             'date_of_joining': '2021-07-12',
             'department': 'Some Department',
             'location': 'Some Location',
             'work_address': 'Some Work Address',
             'permission': 'Some Permission',
             'department_id': 1,
             'employee_id': 100,
             'location_id': 1,
             'address_id': 1,
             'skill_id': 1,
             'permission_id': 1
             },
            {'name': 'Some Name2',
             'surname': 'Some Surname2',
             'date_of_birth': '1999-01-01',
             'salary': 444.44,
             'email': 'some.email2@gmail.com',
             'phone': '375292002400',
             'date_of_joining': '2021-07-12',
             'department': 'Some Department2',
             'location': 'Some Location2',
             'work_address': 'Some Work Address2',
             'permission': 'Some Permission2',
             'department_id': 1,
             'employee_id': 101,
             'location_id': 1,
             'address_id': 1,
             'skill_id': 1,
             'permission_id': 1
             }]
        response = EmployeeList.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json[0]['name'], 'Some Name')
        self.assertEqual(response.json[0]['surname'], 'Some Surname')
        self.assertEqual(response.json[0]['date_of_birth'], '1999-01-01')
        self.assertEqual(response.json[0]['salary'], 444.44)
        self.assertEqual(response.json[0]['email'], 'some.email@gmail.com')
        self.assertEqual(response.json[0]['phone'], '375292002400')
        self.assertEqual(response.json[0]['date_of_joining'], '2021-07-12')
        self.assertEqual(response.json[0]['department'], 'Some Department')
        self.assertEqual(response.json[0]['location'], 'Some Location')
        self.assertEqual(response.json[0]['work_address'], 'Some Work Address')
        self.assertEqual(response.json[0]['permission'], 'Some Permission')
        self.assertEqual(response.json[0]['department_id'], 1)
        self.assertEqual(response.json[0]['employee_id'], 100)
        self.assertEqual(response.json[0]['skill_id'], 1)
        self.assertEqual(response.json[0]['location_id'], 1)
        self.assertEqual(response.json[0]['address_id'], 1)
        self.assertEqual(response.json[0]['permission_id'], 1)
