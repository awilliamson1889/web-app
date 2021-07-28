import unittest
import datetime
from department_app import create_app
from department_app.models.app_models import db, Employee
from department_app.tests.factoryes.employee_factory import EmployeeFactory

app = create_app('Test')
app.app_context().push()


class TestApiEmployee(unittest.TestCase):
    """ doc str """
    def setUp(self):
        """ doc str """
        self.app = app.test_client()
        test_emp = EmployeeFactory()
        test_data = {'name': test_emp.name, 'surname': test_emp.surname, 'date_of_birth': test_emp.date_of_birth,
                     'salary': test_emp.salary, 'email': test_emp.email, 'phone': test_emp.phone,
                     'date_of_joining': test_emp.date_of_joining, 'department': test_emp.department,
                     'location': test_emp.location, 'work_address': test_emp.work_address,
                     'key_skill': test_emp.key_skill, 'permission': test_emp.permission}
        employee = Employee(**test_data)
        db.session.add(employee)
        db.session.commit()
        db.create_all()

    def tearDown(self):
        emp = Employee.query.order_by(Employee.id).all()
        db.session.delete(emp[-1])
        db.session.commit()

    def test_get_employee(self):
        emp = Employee.query.order_by(Employee.id).all()
        last_emp = emp[-1]
        url = f"/api/employee/{last_emp.id}"
        client = app.test_client()
        response = client.get(url)

        self.assertEqual(200, response.status_code)
        self.assertEqual(last_emp.id, response.json['id'])
        self.assertEqual(last_emp.name, response.json['name'])
        self.assertEqual(last_emp.date_of_birth, response.json['date_of_birth'])
        self.assertEqual(last_emp.salary, response.json['salary'])
        self.assertEqual(last_emp.email, response.json['email'])
        self.assertEqual(last_emp.phone, response.json['phone'])
        self.assertEqual(last_emp.date_of_joining, response.json['date_of_joining'])
        self.assertEqual(last_emp.department, response.json['department'])
        self.assertEqual(last_emp.work_address, response.json['work_address'])
        self.assertEqual(last_emp.key_skill, response.json['key_skill'])

    def test_get_employee_not_exist(self):
        employee_id = 999999999
        client = app.test_client()
        url = f"/api/employee/{employee_id}"
        message = f"Could not find employee with ID: {employee_id}."
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_str_id_format(self):
        employee_id = "one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/employee/{employee_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_negative_num_id_format(self):
        employee_id = -1
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/employee/{employee_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_str_num_id_format(self):
        employee_id = "1one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/employee/{employee_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_float_num_id_format(self):
        employee_id = 1.0
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/employee/{employee_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_employee(self):
        emp = Employee.query.order_by(Employee.id).all()
        test_emp = EmployeeFactory()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'name': 'update_test_name', 'surname': 'update_test_surname', 'date_of_birth': '1998-01-01',
                            'salary': 55555.0, 'email': 'update_test_mail@testig.test', 'phone': '55555555555',
                            'date_of_joining': '2021-01-01', 'department': test_emp.department,
                            'location': test_emp.location, 'work_address': test_emp.work_address,
                            'key_skill': test_emp.key_skill, 'permission': test_emp.permission}
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(201, response.status_code)
        self.assertEqual(last_emp.id, response.json['id'])
        self.assertEqual(update_test_data['name'], response.json['name'])
        self.assertEqual(update_test_data['surname'], response.json['surname'])
        self.assertEqual(update_test_data['date_of_birth'], response.json['date_of_birth'])
        self.assertEqual(update_test_data['salary'], response.json['salary'])
        self.assertEqual(update_test_data['email'], response.json['email'])
        self.assertEqual(update_test_data['phone'], response.json['phone'])
        self.assertEqual(update_test_data['date_of_joining'], response.json['date_of_joining'])
        self.assertEqual(update_test_data['department'], response.json['department'])
        self.assertEqual(update_test_data['work_address'], response.json['work_address'])
        self.assertEqual(update_test_data['key_skill'], response.json['key_skill'])

    def test_put_employee_not_exist(self):
        employee_id = 999999999
        client = app.test_client()
        url = f"/api/employee/{employee_id}"
        message = f"Could not find employee with ID: {employee_id}."
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_str_id_format(self):
        employee_id = "one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/employee/{employee_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_negative_num_id_format(self):
        employee_id = -1
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/employee/{employee_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_str_num_id_format(self):
        employee_id = "1one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/employee/{employee_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_float_num_id_format(self):
        employee_id = 1.0
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/employee/{employee_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_big_employee_name(self):
        emp = Employee.query.order_by(Employee.id).all()
        last_emp = emp[-1]
        client = app.test_client()
        update_test_data = {'name': 'test_very_big_name_test_very_big_name_test_very_big_name_test_very_big_name_'
                                    'test_very_big_name_test_very_big_name_test_very_big_name_test_very_big_name'}
        message = "Exception: 1 validation error for EmployeeModel\nname\n  Name length too big! (type=value_error)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_big_employee_surname(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'surname': 'test_very_big_surname_test_very_big_surname_test_very_big_surname_'
                                       'test_very_big_surname_test_very_big_surname_test_very_big_surname'}
        message = "Exception: 1 validation error for EmployeeModel\nsurname\n  " \
                  "Surname length too big! (type=value_error)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_employee_wrong_age(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'date_of_birth': str(datetime.date.today())}
        message = "Exception: 1 validation error for EmployeeModel\n" \
                  "date_of_birth\n  The employee cannot be under the age of 18! (type=value_error)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_employee_date_of_birth_wrong_format(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'date_of_birth': "12-12-2002"}
        message = f"Exception: 1 validation error for EmployeeModel\ndate_of_birth\n  " \
                  f"time data '{update_test_data['date_of_birth']}' does not match format '%Y-%m-%d' (type=value_error)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_employee_date_of_birth_wrong_str_format(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'date_of_birth': "01 Jan 1999"}
        message = f"Exception: 1 validation error for EmployeeModel\ndate_of_birth\n  " \
                  f"time data '{update_test_data['date_of_birth']}' does not match format '%Y-%m-%d' (type=value_error)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_employee_date_of_birth_wrong_num_format(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'date_of_birth': 500000}
        message = f"Exception: 1 validation error for EmployeeModel\ndate_of_birth\n  " \
                  f"time data '{update_test_data['date_of_birth']}' does not match format '%Y-%m-%d' (type=value_error)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_employee_salary_wrong_format(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'salary': "zero"}
        message = "Exception: 1 validation error for EmployeeModel\n" \
                  "salary\n  value is not a valid float (type=type_error.float)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_employee_email_already_exist(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'email': last_emp.email}
        message = "Exception: 1 validation error for EmployeeModel\n" \
                  "email\n  This email is already in use! (type=value_error)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_employee_email_wrong_format(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'email': "test_mail"}
        message = "Exception: 1 validation error for EmployeeModel\n" \
                  "email\n  Check the correctness of the email! (type=value_error)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_employee_phone_wrong_format(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'phone': "one-two-one"}
        message = "Exception: 1 validation error for EmployeeModel\n" \
                  "phone\n  The number must contain only digits! (type=value_error)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_employee_phone_already_exist(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'phone': last_emp.phone}
        message = "Exception: 1 validation error for EmployeeModel\n" \
                  "phone\n  This number is already in use! (type=value_error)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_employee_date_of_joining_wrong_str_format(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'date_of_joining': "01 Jan 1999"}
        message = f"Exception: 1 validation error for EmployeeModel\ndate_of_joining\n  " \
                  f"time data '{update_test_data['date_of_joining']}' does not match format '%Y-%m-%d' (type=value_error)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_employee_date_of_joining_wrong_num_format(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'date_of_joining': 500000}
        message = f"Exception: 1 validation error for EmployeeModel\ndate_of_joining\n  " \
                  f"time data '{update_test_data['date_of_joining']}' " \
                  "does not match format '%Y-%m-%d' (type=value_error)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_department_not_exist(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'department': 999999999}
        message = "Exception: 1 validation error for EmployeeModel\ndepartment\n  " \
                  "There is no such department! See the list of departments: " \
                  ".../swagger/#/Department32API (type=value_error)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_department_wrong_format(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'department': 'RD Lab'}
        message = "Exception: 1 validation error for EmployeeModel\ndepartment\n  " \
                  "value is not a valid integer (type=type_error.integer)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_location_not_exist(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'location': 999999999}
        message = "Exception: 1 validation error for EmployeeModel\nlocation\n  " \
                  "There is no such department! See the list of departments: " \
                  ".../swagger/#/Location32API (type=value_error)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_location_wrong_format(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'location': 'Brest'}
        message = "Exception: 1 validation error for EmployeeModel\nlocation\n  " \
                  "value is not a valid integer (type=type_error.integer)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_work_address_not_exist(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'work_address': 999999999}
        message = "Exception: 1 validation error for EmployeeModel\nwork_address\n  " \
                  "There is no such department! See the list of departments: " \
                  ".../swagger/#/Address32API (type=value_error)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_work_address_wrong_format(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'work_address': 'Moskovskaja, 348'}
        message = "Exception: 1 validation error for EmployeeModel\nwork_address\n  " \
                  "value is not a valid integer (type=type_error.integer)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_key_skill_not_exist(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'key_skill': 999999999}
        message = "Exception: 1 validation error for EmployeeModel\nkey_skill\n  " \
                  "There is no such department! See the list of departments: " \
                  ".../swagger/#/Skill32API (type=value_error)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_key_skill_wrong_format(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'key_skill': 'Python'}
        message = "Exception: 1 validation error for EmployeeModel\nkey_skill\n  " \
                  "value is not a valid integer (type=type_error.integer)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_permission_not_exist(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'permission': 999999999}
        message = "Exception: 1 validation error for EmployeeModel\npermission\n  " \
                  "There is no such department! See the list of departments: " \
                  ".../swagger/#/Permission32API (type=value_error)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_permission_wrong_format(self):
        emp = Employee.query.order_by(Employee.id).all()
        client = app.test_client()
        last_emp = emp[-1]
        update_test_data = {'permission': 'Administrator'}
        message = "Exception: 1 validation error for EmployeeModel\npermission\n  " \
                  "value is not a valid integer (type=type_error.integer)"
        url = f"/api/employee/{last_emp.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_delete_employee(self):
        test_emp = EmployeeFactory()
        client = app.test_client()
        test_data = {'name': test_emp.name, 'surname': test_emp.surname, 'date_of_birth': test_emp.date_of_birth,
                     'salary': test_emp.salary, 'email': test_emp.email + "test", 'phone': test_emp.phone,
                     'date_of_joining': test_emp.date_of_joining, 'department': test_emp.department,
                     'location': test_emp.location, 'work_address': test_emp.work_address,
                     'key_skill': test_emp.key_skill, 'permission': test_emp.permission}
        employee = Employee(**test_data)
        db.session.add(employee)
        db.session.commit()
        url = f"/api/employee/{employee.id}"
        response = client.delete(url)
        self.assertEqual(response.status_code, 204)

        url_check = f"/api/employee/{employee.id}"
        message = f"Could not find employee with ID: {employee.id}."
        response_check = client.get(url_check)
        self.assertEqual(response_check.status_code, 404)
        self.assertEqual(message, response_check.json['message'])

    def test_post_employee(self):
        test_emp = EmployeeFactory()
        client = app.test_client()
        test_data = {'name': test_emp.name, 'surname': test_emp.surname, 'date_of_birth': test_emp.date_of_birth,
                     'salary': test_emp.salary, 'email': test_emp.email, 'phone': test_emp.phone,
                     'date_of_joining': test_emp.date_of_joining, 'department': test_emp.department,
                     'location': test_emp.location, 'work_address': test_emp.work_address,
                     'key_skill': test_emp.key_skill, 'permission': test_emp.permission}
        url = f"/api/employee"
        response = client.post(url, json=test_data)

        emp = Employee.query.order_by(Employee.id).all()
        last_emp = emp[-1]
        self.assertEqual(last_emp.name, response.json['name'])
        self.assertEqual(last_emp.surname, response.json['surname'])
        self.assertEqual(response.status_code, 201)
        db.session.delete(last_emp)
        db.session.commit()

    def test_get_employee_all(self):
        url = f"/api/employee"
        client = app.test_client()
        response = client.get(url)
        employees = Employee.query.order_by(Employee.id).all()
        self.assertEqual(len(response.json), len(employees))

    def test_employee_api_put_wrong_salary_format(self):
        test_data = {'salary': -10000}
        emp = Employee.query.order_by(Employee.id).all()
        last_emp = emp[-1]
        client = app.test_client()
        url = f'/api/employee/{last_emp.id}'
        message = "Exception: 1 validation error for EmployeeModel\n" \
                  "salary\n  Salary less then 0! (type=value_error)"
        response = client.put(url, json=test_data)

        self.assertEqual(response.json['message'], message)
        self.assertEqual(response.status_code, 404)
