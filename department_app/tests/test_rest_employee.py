import unittest
import requests
import tempfile
from department_app import create_app
from department_app.models.app_models import db, Employee

app = create_app()
app.app_context().push()


class TestApiEmployee(unittest.TestCase):
    """ doc str """
    # API_URL = "http://127.0.0.1:5000/api"
    # EMPLOYEES_URL = "{}/employee".format(API_URL)  # All employee URL / create employee URL (NORMAL)
    # EMPLOYEE1_URL = "{}/employee/1".format(API_URL)  # Employee with id 1 URL (NORMAL)
    # EMPLOYEE2_URL = "{}/employee/7878".format(API_URL)  # Employee with id 7878 URL (WRONG)
    # EMPLOYEE3_URL = "{}/employee/sage".format(API_URL)  # Employee with id sage URL (WRONG)
    #
    # EMPLOYEE_TEST_DATA1 = {
    #     "date_of_birth": "1999-12-12",
    #     "date_of_joining": "2020-12-12",
    #     "department": 1,
    #     "email": "TEST_MAIL@TESTMAIL.COM",
    #     "key_skill": 1,
    #     "location": 1,
    #     "name": "TEST_NAME",
    #     "permission": 1,
    #     "phone": "111111111111",
    #     "salary": 9999.9,
    #     "surname": "TEST_SURNAME",
    #     "work_address": 1
    # }
    #
    # EMPLOYEE_TEST_DATA2 = {
    #     "date_of_birth": "1999-12-12",
    #     "date_of_joining": "2020-12-12",
    #     "department": 1,
    #     "email": "TEST_MAIL@TESTMAIL.COM",
    #     "key_skill": 1,
    #     "location": 1,
    #     "name": "VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME "
    #             "VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME",
    #     "permission": 1,
    #     "phone": "111111111111",
    #     "salary": 9999.9,
    #     "surname": "TEST_SURNAME",
    #     "work_address": 1
    # }
    #
    # old_len = len((requests.get(EMPLOYEES_URL).json()))
    #
    def SetUp(self):
        """ doc str """
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://flask_admin:admin1111@localhost:5432/flask_app"
        self.app = app.test_client()
        db.create_all()

    def test_get_employee(self):
        test_data = {'name': 'test_name', 'surname': 'test_surname', 'date_of_birth': '01-01-1999', 'salary': 0,
                     'email': 'test_mail@testig.test', 'phone': '00000000000', 'date_of_joining': '01-01-2020',
                     'department': 1, 'location': 1, 'work_address': 1, 'key_skill': 1, 'permission': 1}
        employee = Employee(**test_data)
        db.session.add(employee)
        db.session.commit()
        url = f"http://127.0.0.1:5000/api/employee/{employee.id}"
        response = requests.get(url)
        try:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(employee.id, response.json()['id'])
            self.assertEqual(employee.name, response.json()['name'])
            self.assertEqual('Fri, 01 Jan 1999 00:00:00 GMT', response.json()['date_of_birth'])
            self.assertEqual(employee.salary, response.json()['salary'])
            self.assertEqual(employee.email, response.json()['email'])
            self.assertEqual(employee.phone, response.json()['phone'])
            self.assertEqual('Wed, 01 Jan 2020 00:00:00 GMT', response.json()['date_of_joining'])
            self.assertEqual(employee.department, response.json()['department'])
            self.assertEqual(employee.work_address, response.json()['work_address'])
            self.assertEqual(employee.key_skill, response.json()['key_skill'])
        finally:
            db.session.delete(employee)
            db.session.commit()

    def test_get_employee_not_exist(self):
        employee_id = 999999999
        url = f"http://127.0.0.1:5000/api/employee/{employee_id}"
        message = f"Could not find employee with ID: {employee_id}."
        response = requests.get(url)
        self.assertEqual(message, response.json()['message'])

    def test_get_wrong_id_format(self):
        employee_id = "one"
        message = "ID must be a number."

        url = f"http://127.0.0.1:5000/api/employee/{employee_id}"
        response = requests.get(url)
        self.assertEqual(message, response.json()['message'])

        employee_id = -1
        url = f"http://127.0.0.1:5000/api/employee/{employee_id}"
        response = requests.get(url)
        self.assertEqual(message, response.json()['message'])

        employee_id = "1one"
        url = f"http://127.0.0.1:5000/api/employee/{employee_id}"
        response = requests.get(url)
        self.assertEqual(message, response.json()['message'])

        employee_id = 1.0
        url = f"http://127.0.0.1:5000/api/employee/{employee_id}"
        response = requests.get(url)
        self.assertEqual(message, response.json()['message'])

    def test_put_employee(self):
        test_data = {'name': 'test_name', 'surname': 'test_surname', 'date_of_birth': '01-01-1999', 'salary': 0,
                     'email': 'test_mail@testig.test', 'phone': '00000000000', 'date_of_joining': '01-01-2020',
                     'department': 1, 'location': 1, 'work_address': 1, 'key_skill': 1, 'permission': 1}
        update_test_data = {'name': 'update_test_name', 'surname': 'update_test_surname', 'date_of_birth': '01-01-1999',
                            'salary': 55555, 'email': 'update_test_mail@testig.test', 'phone': '55555555555',
                            'date_of_joining': '01-01-2020', 'department': 1, 'location': 1, 'work_address': 1,
                            'key_skill': 1, 'permission': 1}
        employee = Employee(**test_data)
        db.session.add(employee)
        db.session.commit()
        url = f"http://127.0.0.1:5000/api/employee/{employee.id}"
        response = requests.put(url, json=update_test_data)
        try:
            # self.assertEqual(response.status_code, 200)
            self.assertEqual(employee.id, response.json()['id'])
            self.assertEqual(update_test_data['name'], response.json()['name'])
            self.assertEqual('Fri, 01 Jan 1999 00:00:00 GMT', response.json()['date_of_birth'])
            self.assertEqual(employee.salary, response.json()['salary'])
            self.assertEqual(employee.email, response.json()['email'])
            self.assertEqual(employee.phone, response.json()['phone'])
            self.assertEqual('Wed, 01 Jan 2020 00:00:00 GMT', response.json()['date_of_joining'])
            self.assertEqual(employee.department, response.json()['department'])
            self.assertEqual(employee.work_address, response.json()['work_address'])
            self.assertEqual(employee.key_skill, response.json()['key_skill'])
        finally:
            db.session.delete(employee)
            db.session.commit()




    #
    # # def tearDown(self):
    # #     db.session.remove()
    # #     db.drop_all()
    #
    # def test_get_all_employee(self):
    #     """ doc str """
    #     response = requests.get(TestApiEmployee.EMPLOYEES_URL)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(response.json()), len(Employee.query.all()))
    #
    # def test_wrong_employee_id(self):
    #     """ doc str """
    #     response = requests.get(TestApiEmployee.EMPLOYEE3_URL)
    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(response.json()['message'], "ID must be a number.")
    #
    # def test_employee_not_exist(self):
    #     """ doc str """
    #     response = requests.get(TestApiEmployee.EMPLOYEE2_URL)
    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(response.json()['message'], "Could not find employee with ID: 7878.")
    #
    # # def test_create_employee(self):
    # #     r = requests.post(TestApiEmployee.EMPLOYEES_URL, json=TestApiEmployee.EMPLOYEE_TEST_DATA1)
    # #     self.assertEqual(TestApiEmployee.old_len + 1, len(Employee.query.all()))
    # #     self.assertEqual(r.status_code, 201)
    # #
    # # def test_delete_employee(self):
    # #     r = requests.delete(TestApiEmployee.EMPLOYEES_URL+"/109")
    # #     self.assertEqual(TestApiEmployee.old_len - 1, len(Employee.query.all()))
    # #     self.assertEqual(r.status_code, 204)
    #
    # def test_wrong_employee_name_length_post(self):
    #     """ doc str """
    #     response = requests.post(TestApiEmployee.EMPLOYEES_URL, json=TestApiEmployee.EMPLOYEE_TEST_DATA2)
    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(response.json()['message'], "Exception: 1 validation error for EmployeeModel\n"
    #                                           "name\n  Name length too big! (type=value_error)")
    #
    # def test_wrong_employee_name_length_put(self):
    #     """ doc str """
    #     response = requests.put(TestApiEmployee.EMPLOYEE1_URL, json={"name": "VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME "
    #                                                                   "VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME "
    #                                                                   "VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME "
    #                                                                   "VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME "
    #                                                                   "VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME"})
    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(response.json()['message'], "Exception: 1 validation error for EmployeeModel\n"
    #                                           "name\n  Name length too big! (type=value_error)")
