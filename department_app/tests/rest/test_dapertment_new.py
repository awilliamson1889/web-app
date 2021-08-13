from unittest.mock import patch
import unittest

from department_app.rest import Department, DepartmentList
from department_app.tests import DepartmentFactory


class TestApiDepartment(unittest.TestCase):
    """Test department api class"""

    @patch('department_app.rest.department.CRUDDepartment.get_department')
    def test_get_department(self, mock_get_department):
        """Api should return information about department."""
        mock_get_department.return_value = {'name': 'Some Department',
                                            'manager': 'Some Manager',
                                            'date_of_creation': '2021-01-01',
                                            'emp_count': 40,
                                            'dep_id': 1}
        response = Department.get(100)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Some Department')
        self.assertEqual(response.json['manager'], 'Some Manager')
        self.assertEqual(response.json['date_of_creation'], '2021-01-01')
        self.assertEqual(response.json['emp_count'], 40)
        self.assertEqual(response.json['dep_id'], 1)

    @patch('department_app.rest.department.CRUDDepartment.update_department')
    def test_put_department(self, mock_update_department):
        """Api should return information about department."""
        mock_update_department.return_value = {'name': 'Updated Department',
                                               'manager': 'Updated Manager',
                                               'date_of_creation': '2021-01-01'}
        response = Department.put(100)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], 'Updated Department')
        self.assertEqual(response.json['manager'], 'Updated Manager')
        self.assertEqual(response.json['date_of_creation'], '2021-01-01')

    @patch('department_app.rest.department.CRUDDepartment.create_department')
    def test_post_department(self, mock_create_department):
        """Api should return information about department."""
        mock_create_department.return_value = {'name': 'New Department',
                                               'manager': 'New Manager',
                                               'date_of_creation': '2021-01-01'}
        response = DepartmentList.post()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], 'New Department')
        self.assertEqual(response.json['manager'], 'New Manager')
        self.assertEqual(response.json['date_of_creation'], '2021-01-01')

    @patch('department_app.rest.department.CRUDDepartment.get_all_department')
    def test_get_all_department(self, mock_get_all_department):
        """Api should return information about department."""
        mock_get_all_department.return_value = [
            {
                'name': 'Some Department1',
                'manager': 'Some Manager1',
                'date_of_creation': '2021-01-01',
                'emp_count': 40,
                'dep_id': 1
             },
            {
                'name': 'Some Department2',
                'manager': 'Some Manager2',
                'date_of_creation': '2021-02-02',
                'emp_count': 60,
                'dep_id': 2
             },
            {
                'name': 'Some Department3',
                'manager': 'Some Manager3',
                'date_of_creation': '2021-03-03',
                'emp_count': 80,
                'dep_id': 3
             }]
        response = DepartmentList.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 3)
        self.assertEqual(response.json[0]['name'], 'Some Department1')
        self.assertEqual(response.json[0]['manager'], 'Some Manager1')
        self.assertEqual(response.json[0]['date_of_creation'], '2021-01-01')
        self.assertEqual(response.json[0]['emp_count'], 40)
        self.assertEqual(response.json[0]['dep_id'], 1)
