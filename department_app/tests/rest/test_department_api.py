import unittest
from department_app import create_app
from department_app.models.app_models import db, Department
from department_app.tests.factoryes.department_factory import DepartmentFactory

app = create_app('Test')
app.app_context().push()


class TestApiDepartment(unittest.TestCase):
    """ doc str """
    def setUp(self):
        """ doc str """
        self.app = app.test_client()
        test_department = DepartmentFactory()
        test_data = {'name': test_department.name, 'manager': test_department.manager,
                     'date_of_creation': test_department.date_of_creation}
        department = Department(**test_data)
        db.session.add(department)
        db.session.commit()
        db.create_all()

    def tearDown(self):
        department = Department.query.order_by(Department.id).all()
        db.session.delete(department[-1])
        db.session.commit()

    def test_get_department(self):
        department = Department.query.order_by(Department.id).all()
        last_department = department[-1]
        url = f"/api/department/{last_department.id}"
        client = app.test_client()
        response = client.get(url)

        self.assertEqual(200, response.status_code)
        self.assertEqual(last_department.id, response.json['id'])
        self.assertEqual(last_department.name, response.json['name'])
        self.assertEqual(last_department.manager, response.json['manager'])

    def test_get_department_not_exist(self):
        department_id = 999999999
        client = app.test_client()
        url = f"/api/department/{department_id}"
        message = f"Could not find department with ID: {department_id}."
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_str_id_format(self):
        department_id = "one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/department/{department_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_negative_num_id_format(self):
        department_id = -1
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/department/{department_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_str_num_id_format(self):
        department_id = "1one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/department/{department_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_float_num_id_format(self):
        department_id = 1.0
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/department/{department_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_department(self):
        department = Department.query.order_by(Department.id).all()
        client = app.test_client()
        last_department = department[-1]
        update_test_data = {'name': 'update_test_department', 'manager': 'update_manager',
                            'date_of_creation': '2022-01-11'}
        url = f"/api/department/{last_department.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(201, response.status_code)
        self.assertEqual(last_department.id, response.json['id'])
        self.assertEqual(update_test_data['name'], response.json['name'])
        self.assertEqual(update_test_data['manager'], response.json['manager'])
        self.assertEqual(update_test_data['date_of_creation'], response.json['date_of_creation'])  # !!!

    def test_put_department_not_exist(self):
        department_id = 999999999
        client = app.test_client()
        url = f"/api/department/{department_id}"
        message = f"Could not find department with ID: {department_id}."
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_str_id_format(self):
        department_id = "one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/department/{department_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_negative_num_id_format(self):
        department_id = -1
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/department/{department_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_str_num_id_format(self):
        department_id = "1one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/department/{department_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_float_num_id_format(self):
        department_id = 1.0
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/department/{department_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_big_department_name(self):
        department = Department.query.order_by(Department.id).all()
        last_department = department[-1]
        client = app.test_client()
        update_test_data = {'name': 'test_very_big_department_test_very_big_department_test_very_big_department_'
                                    'test_very_big_department_test_very_big_department_test_very_big_department'}
        message = "Exception: 1 validation error for DepartmentSchema\nname\n  Name length too big! (type=value_error)"
        url = f"/api/department/{last_department.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_big_department_manager(self):
        department = Department.query.order_by(Department.id).all()
        last_department = department[-1]
        client = app.test_client()
        update_test_data = {'manager': 'test_very_big_department_manager_test_very_big_department_manager_'
                                       'test_very_big_department_manager_test_very_big_department_manager_'
                                       'test_very_big_department_manager_test_very_big_department_manager_'}
        message = "Exception: 1 validation error for DepartmentSchema\nmanager\n  Manager name length too big! " \
                  "(type=value_error)"
        url = f"/api/department/{last_department.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_department_already_exist(self):
        department = Department.query.order_by(Department.id).all()
        client = app.test_client()
        last_department = department[-1]
        update_test_data = {'name': last_department.name}
        message = "Exception: 1 validation error for DepartmentSchema\n" \
                  "name\n  This department is already in use! (type=value_error)"
        url = f"/api/department/{last_department.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_post_department(self):
        test_department = DepartmentFactory()
        client = app.test_client()
        test_data = {'name': test_department.name, 'manager': test_department.manager,
                     'date_of_creation': test_department.date_of_creation}
        url = f"/api/department"
        response = client.post(url, json=test_data)
        self.assertEqual(response.status_code, 201)
        department = Department.query.order_by(Department.id).all()
        last_department = department[-1]
        db.session.delete(last_department)
        db.session.commit()

    def test_get_department_all(self):
        url = f"/api/department"
        client = app.test_client()
        response = client.get(url)
        department = Department.query.order_by(Department.id).all()
        self.assertEqual(len(response.json), len(department))

    def test_post_department_very_long_name(self):
        test_department = DepartmentFactory()
        client = app.test_client()
        test_data = {'name': 'test_very_big_department_test_very_big_department_test_very_big_department_'
                             'test_very_big_department_test_very_big_department_test_very_big_department',
                     'manager': test_department.manager,
                     'date_of_creation': test_department.date_of_creation}
        message = "Exception: 1 validation error for DepartmentSchema\nname\n  Name length too big! (type=value_error)"
        url = f"/api/department"
        response = client.post(url, json=test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_post_department_very_long_manager_name(self):
        test_department = DepartmentFactory()
        client = app.test_client()
        test_data = {'name': test_department.name,
                     'manager': 'test_very_big_manager_name_test_very_big_manager_name_test_very_big_manager_name_'
                                'test_very_big_manager_name_test_very_big_manager_name_test_very_big_manager_name',
                     'date_of_creation': test_department.date_of_creation}
        message = "Exception: 1 validation error for DepartmentSchema\nmanager\n" \
                  "  Manager name length too big! (type=value_error)"
        url = f"/api/department"
        response = client.post(url, json=test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])
