import os
import unittest
import requests
from flask import jsonify
from department_app import create_app
from department_app.models.app_models import db, Employee

app = create_app()
app.app_context().push()


class TestApiEmployee(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/api"
    EMPLOYEES_URL = "{}/employee".format(API_URL)  # All employee URL / create employee URL (NORMAL)
    EMPLOYEE1_URL = "{}/employee/1".format(API_URL)  # Employee with id 1 URL (NORMAL)
    EMPLOYEE2_URL = "{}/employee/7878".format(API_URL)  # Employee with id 7878 URL (WRONG)
    EMPLOYEE3_URL = "{}/employee/sage".format(API_URL)  # Employee with id sage URL (WRONG)

    EMPLOYEE_TEST_DATA1 = {
        "date_of_birth": "1999-12-12",
        "date_of_joining": "2020-12-12",
        "department": 1,
        "email": "TEST_MAIL@TESTMAIL.COM",
        "key_skill": 1,
        "location": 1,
        "name": "TEST_NAME",
        "permission": 1,
        "phone": "111111111111",
        "salary": 9999.9,
        "surname": "TEST_SURNAME",
        "work_address": 1
    }

    EMPLOYEE_TEST_DATA2 = {
        "date_of_birth": "1999-12-12",
        "date_of_joining": "2020-12-12",
        "department": 1,
        "email": "TEST_MAIL@TESTMAIL.COM",
        "key_skill": 1,
        "location": 1,
        "name": "VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME "
                "VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME",
        "permission": 1,
        "phone": "111111111111",
        "salary": 9999.9,
        "surname": "TEST_SURNAME",
        "work_address": 1
    }

    old_len = len((requests.get(EMPLOYEES_URL).json()))

    def SetUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://flask_admin:admin1111@localhost:5432/flask_app"
        self.app = app.test_client()
        db.create_all()

    # def tearDown(self):``
    #     db.session.remove()
    #     db.drop_all()

    def test_get_all_employee(self):
        r = requests.get(TestApiEmployee.EMPLOYEES_URL)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), len(Employee.query.all()))

    def test_wrong_employee_id(self):
        r = requests.get(TestApiEmployee.EMPLOYEE3_URL)
        self.assertEqual(r.status_code, 404)
        self.assertEqual(r.json()['message'], "ID must be a number.")

    def test_employee_not_exist(self):
        r = requests.get(TestApiEmployee.EMPLOYEE2_URL)
        self.assertEqual(r.status_code, 404)
        self.assertEqual(r.json()['message'], "Could not find employee with ID: 7878.")

    # def test_create_employee(self):
    #     r = requests.post(TestApiEmployee.EMPLOYEES_URL, json=TestApiEmployee.EMPLOYEE_TEST_DATA1)
    #     self.assertEqual(TestApiEmployee.old_len + 1, len(Employee.query.all()))
    #     self.assertEqual(r.status_code, 201)
    #
    # def test_delete_employee(self):
    #     r = requests.delete(TestApiEmployee.EMPLOYEES_URL+"/109")
    #     self.assertEqual(TestApiEmployee.old_len - 1, len(Employee.query.all()))
    #     self.assertEqual(r.status_code, 204)

    def test_wrong_employee_name_length_post(self):
        r = requests.post(TestApiEmployee.EMPLOYEES_URL, json=TestApiEmployee.EMPLOYEE_TEST_DATA2)
        self.assertEqual(r.status_code, 404)
        self.assertEqual(r.json()['message'], "Exception: 1 validation error for EmployeeModel\n"
                                              "name\n  Name length too big! (type=value_error)")

    def test_wrong_employee_name_length_put(self):
        r = requests.put(TestApiEmployee.EMPLOYEE1_URL, json={"name": "VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME "
                                                                      "VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME "
                                                                      "VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME "
                                                                      "VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME "
                                                                      "VERY_BIG_TEST_NAME VERY_BIG_TEST_NAME"})
        self.assertEqual(r.status_code, 404)
        self.assertEqual(r.json()['message'], "Exception: 1 validation error for EmployeeModel\n"
                                              "name\n  Name length too big! (type=value_error)")

