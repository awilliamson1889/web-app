# import json
# import os
# import tempfile
# from flask import jsonify
# import pytest
# import datetime
#
# from department_app import create_app, db
# from department_app.models.app_models import Employee
# from department_app.models.factoryes.employee_factory import EmployeeFactory
# from department_app import create_app
#
# app = create_app()
# app.app_context().push()
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/flask_app_test'
#
#
# def setup():
#     test_emp = EmployeeFactory()
#     test_data = {'name': test_emp.name, 'surname': test_emp.surname, 'date_of_birth': test_emp.date_of_birth,
#                  'salary': test_emp.salary, 'email': test_emp.email, 'phone': test_emp.phone,
#                  'date_of_joining': test_emp.date_of_joining, 'department': test_emp.department,
#                  'location': test_emp.location, 'work_address': test_emp.work_address,
#                  'key_skill': test_emp.key_skill, 'permission': test_emp.permission}
#     return test_data
#
#
#
# # def test_employee_api_post():
# #     client = app.test_client()
# #     url = '/api/employee'
# #     test_data = setup()
# #     response = client.post(url, json=test_data)
# #
# #     assert response.json['date_of_joining'] == test_data['date_of_joining']
# #     assert response.json['date_of_birth'] == test_data['date_of_birth']
# #     assert response.json['work_address'] == test_data['work_address']
# #     assert response.json['department'] == test_data['department']
# #     assert response.json['permission'] == test_data['permission']
# #     assert response.json['key_skill'] == test_data['key_skill']
# #     assert response.json['email'].lower() == test_data['email']
# #     assert response.json['location'] == test_data['location']
# #     assert response.json['surname'] == test_data['surname']
# #     assert response.json['salary'] == test_data['salary']
# #     assert response.json['phone'] == test_data['phone']
# #     assert response.json['name'] == test_data['name']
# #     assert response.status_code == 201
# #
# #
# # def test_employee_api_get():
# #     client = app.test_client()
# #     employee = Employee.query.filter_by(id=4).first()
# #     employee_id = 4
# #     url = f'/api/employee/{employee_id}'
# #     response = client.get(url)
# #
# #     # assert response.json['date_of_joining'] == employee.date_of_joining  # ???
# #     # assert response.json['date_of_birth'] == employee.date_of_birth  # ???
# #     assert response.json['work_address'] == employee.work_address
# #     assert response.json['department'] == employee.department
# #     assert response.json['permission'] == employee.permission
# #     assert response.json['key_skill'] == employee.key_skill
# #     assert response.json['email'].lower() == employee.email
# #     assert response.json['location'] == employee.location
# #     assert response.json['surname'] == employee.surname
# #     assert response.json['salary'] == employee.salary
# #     assert response.json['phone'] == employee.phone
# #     assert response.json['name'] == employee.name
# #     assert response.status_code == 200
# #
# #
# # def test_employee_api_get_not_exist():
# #     client = app.test_client()
# #     employee_id = 999999999
# #     url = f'/api/employee/{employee_id}'
# #     message = f"Could not find employee with ID: {employee_id}."
# #     response = client.get(url)
# #
# #     assert response.json['message'] == message
# #     assert response.status_code == 404
# #
# # def test_employee_api_get_wrong_format1():
# #     client = app.test_client()
# #     employee_id = "string id"
# #     url = f'/api/employee/{employee_id}'
# #     message = "ID must be a number."
# #     response = client.get(url)
# #
# #     assert response.json['message'] == message
# #     assert response.status_code == 404
# #
# #
# # def test_employee_api_get_wrong_format2():
# #     client = app.test_client()
# #     employee_id = -15
# #     url = f'/api/employee/{employee_id}'
# #     message = "ID must be a number."
# #     response = client.get(url)
# #
# #     assert response.json['message'] == message
# #     assert response.status_code == 404
# #
# #
# # def test_employee_api_get_wrong_format3():
# #     client = app.test_client()
# #     employee_id = 3.0
# #     url = f'/api/employee/{employee_id}'
# #     message = "ID must be a number."
# #     response = client.get(url)
# #
# #     assert response.json['message'] == message
# #     assert response.status_code == 404
# #
# # def test_employee_api_put():
# #     client = app.test_client()
# #     employee_id = 4
# #     url = f'/api/employee/{employee_id}'
# #     test_data = setup()
# #     response = client.put(url, json=test_data)
# #
# #     # assert response.json['date_of_joining'] == test_data['date_of_joining']  # ???
# #     # assert response.json['date_of_birth'] == test_data['date_of_birth']  # ???
# #     assert response.json['work_address'] == test_data['work_address']
# #     assert response.json['department'] == test_data['department']
# #     assert response.json['permission'] == test_data['permission']
# #     assert response.json['key_skill'] == test_data['key_skill']
# #     assert response.json['email'].lower() == test_data['email']
# #     assert response.json['location'] == test_data['location']
# #     assert response.json['surname'] == test_data['surname']
# #     assert response.json['salary'] == test_data['salary']
# #     assert response.json['phone'] == test_data['phone']
# #     assert response.json['name'] == test_data['name']
# #     assert response.status_code == 201
# #
# # def test_employee_api_put_not_exist():
# #     client = app.test_client()
# #     employee_id = 999999999
# #     url = f'/api/employee/{employee_id}'
# #     message = f"Could not find employee with ID: {employee_id}."
# #     response = client.put(url)
# #
# #     assert response.json['message'] == message
# #     assert response.status_code == 404
# #
# #
# # def test_employee_api_put_wrong_format1():
# #     client = app.test_client()
# #     employee_id = 'employee id'
# #     url = f'/api/employee/{employee_id}'
# #     message = "ID must be a number."
# #     response = client.put(url)
# #
# #     assert response.json['message'] == message
# #     assert response.status_code == 404
# #
# #
# # def test_employee_api_put_wrong_format2():
# #     client = app.test_client()
# #     employee_id = -5
# #     url = f'/api/employee/{employee_id}'
# #     message = "ID must be a number."
# #     response = client.put(url)
# #
# #     assert response.json['message'] == message
# #     assert response.status_code == 404
# #
# #
# # def test_employee_api_put_wrong_format3():
# #     client = app.test_client()
# #     employee_id = 4.5
# #     url = f'/api/employee/{employee_id}'
# #     message = "ID must be a number."
# #     response = client.put(url)
# #
# #     assert response.json['message'] == message
# #     assert response.status_code == 404
# #
# #
# # def test_employee_api_put_wrong_name_format():
# #     test_data = {'name': 'test_very_big_name_test_very_big_name_test_very_big_name_test_very_big_name_'
# #                          'test_very_big_name_test_very_big_name_test_very_big_name_test_very_big_name'}
# #     client = app.test_client()
# #     employee_id = 1
# #     url = f'/api/employee/{employee_id}'
# #     message = "Exception: 1 validation error for EmployeeModel\nname\n  Name length too big! (type=value_error)"
# #     response = client.put(url, json=test_data)
# #
# #     assert response.json['message'] == message
# #     assert response.status_code == 404
# #
# #
# # def test_employee_api_put_wrong_surname_format():
# #     test_data = {'surname': 'test_very_big_surname_test_very_big_surname_test_very_big_surname_'
# #                             'test_very_big_surname_test_very_big_surname_test_very_big_surname'}
# #     client = app.test_client()
# #     employee_id = 1
# #     url = f'/api/employee/{employee_id}'
# #     message = "Exception: 1 validation error for EmployeeModel\nsurname\n  Surname length too big! (type=value_error)"
# #     response = client.put(url, json=test_data)
# #
# #     assert response.json['message'] == message
# #     assert response.status_code == 404
# #
# # def test_employee_api_put_wrong_age_format():
# #     test_data = {'date_of_birth': str(datetime.date.today())}
# #     client = app.test_client()
# #     employee_id = 1
# #     url = f'/api/employee/{employee_id}'
# #     message = "Exception: 1 validation error for EmployeeModel\n" \
# #               "date_of_birth\n  The employee cannot be under the age of 18! (type=value_error)"
# #     response = client.put(url, json=test_data)
# #
# #     assert response.json['message'] == message
# #     assert response.status_code == 404
# #
# # def test_employee_api_put_wrong_date_of_birth_format():
# #     test_data = {'date_of_birth': '12-12-2021'}
# #     client = app.test_client()
# #     employee_id = 1
# #     url = f'/api/employee/{employee_id}'
# #     message = "Exception: 1 validation error for EmployeeModel\ndate_of_birth\n  " \
# #               f"time data '{test_data['date_of_birth']}' does not match format '%Y-%m-%d' (type=value_error)"
# #     response = client.put(url, json=test_data)
# #
# #     assert response.json['message'] == message
# #     assert response.status_code == 404
# #
# #
# # def test_employee_api_put_wrong_salary_format1():
# #     test_data = {'salary': 'employee salary'}
# #     client = app.test_client()
# #     employee_id = 1
# #     url = f'/api/employee/{employee_id}'
# #     message = "Exception: 1 validation error for EmployeeModel\n" \
# #               "salary\n  value is not a valid float (type=type_error.float)"
# #     response = client.put(url, json=test_data)
# #
# #     assert response.json['message'] == message
# #     assert response.status_code == 404
# #
# # def test_employee_api_put_wrong_salary_format2():
# #     test_data = {'salary': -10000}
# #     client = app.test_client()
# #     employee_id = 1
# #     url = f'/api/employee/{employee_id}'
# #     message = "Exception: 1 validation error for EmployeeModel\n" \
# #               "salary\n  Salary less then 0! (type=value_error)"
# #     response = client.put(url, json=test_data)
# #
# #     assert response.json['message'] == message
# #     assert response.status_code == 404
# #
# #
# # def test_employee_api_put_email_already_exist():
# #     employee = Employee.query.filter_by(id=4).first()
# #     test_data = {'email': employee.email}
# #     client = app.test_client()
# #     employee_id = 4
# #     url = f'/api/employee/{employee_id}'
# #     message = "Exception: 1 validation error for EmployeeModel\n" \
# #               "email\n  This email is already in use! (type=value_error)"
# #     response = client.put(url, json=test_data)
# #
# #     assert response.json['message'] == message
# #     assert response.status_code == 404
# #
# # def test_employee_api_put_wrong_email_format():
# #     test_data = {'email': 'new_email'}
# #     client = app.test_client()
# #     employee_id = 4
# #     url = f'/api/employee/{employee_id}'
# #     message = "Exception: 1 validation error for EmployeeModel\n" \
# #               "email\n  Check the correctness of the email! (type=value_error)"
# #     response = client.put(url, json=test_data)
# #
# #     assert response.json['message'] == message
# #     assert response.status_code == 404
#
