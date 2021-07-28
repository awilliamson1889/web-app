import unittest
from department_app import create_app
from department_app.models.app_models import db, Permission
from department_app.models.factoryes.permission_factory import PermissionFactory

app = create_app('Test')
app.app_context().push()


class TestApiPermission(unittest.TestCase):
    """ doc str """
    def setUp(self):
        """ doc str """
        self.app = app.test_client()
        test_permission = PermissionFactory()
        test_data = {'name': test_permission.name}
        permission = Permission(**test_data)
        db.session.add(permission)
        db.session.commit()
        db.create_all()

    def tearDown(self):
        permission = Permission.query.order_by(Permission.id).all()
        db.session.delete(permission[-1])
        db.session.commit()

    def test_get_permission(self):
        permission = Permission.query.order_by(Permission.id).all()
        last_permission = permission[-1]
        url = f"/api/permission/{last_permission.id}"
        client = app.test_client()
        response = client.get(url)

        self.assertEqual(200, response.status_code)
        self.assertEqual(last_permission.id, response.json['id'])
        self.assertEqual(last_permission.name, response.json['name'])

    def test_get_permission_not_exist(self):
        permission_id = 999999999
        client = app.test_client()
        url = f"/api/permission/{permission_id}"
        message = f"Could not find permission with ID: {permission_id}."
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_str_id_format(self):
        permission_id = "one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/permission/{permission_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_negative_num_id_format(self):
        permission_id = -1
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/permission/{permission_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_str_num_id_format(self):
        permission_id = "1one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/permission/{permission_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_float_num_id_format(self):
        permission_id = 1.0
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/permission/{permission_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_permission(self):
        permission = Permission.query.order_by(Permission.id).all()
        client = app.test_client()
        last_permission = permission[-1]
        update_test_data = {'name': 'update_test_permission'}
        url = f"/api/permission/{last_permission.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(201, response.status_code)
        self.assertEqual(last_permission.id, response.json['id'])
        self.assertEqual(update_test_data['name'], response.json['name'])

    def test_put_permission_not_exist(self):
        permission_id = 999999999
        client = app.test_client()
        url = f"/api/permission/{permission_id}"
        message = f"Could not find permission with ID: {permission_id}."
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_str_id_format(self):
        permission_id = "one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/permission/{permission_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_negative_num_id_format(self):
        permission_id = -1
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/permission/{permission_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_str_num_id_format(self):
        permission_id = "1one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/permission/{permission_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_float_num_id_format(self):
        permission_id = 1.0
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/permission/{permission_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_big_permission_name(self):
        permission = Permission.query.order_by(Permission.id).all()
        last_permission = permission[-1]
        client = app.test_client()
        update_test_data = {'name': 'test_very_big_permission_name_test_very_big_permission_name_'
                                    'test_very_big_permission_name_test_very_big_permission_name'}
        message = "Exception: 1 validation error for PermissionModel\nname\n  Name length too big! (type=value_error)"
        url = f"/api/permission/{last_permission.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_permission_already_exist(self):
        permission = Permission.query.order_by(Permission.id).all()
        client = app.test_client()
        last_permission = permission[-1]
        update_test_data = {'name': last_permission.name}
        message = "Exception: 1 validation error for PermissionModel\n" \
                  "name\n  This permission is already in use! (type=value_error)"
        url = f"/api/permission/{last_permission.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_post_permission(self):
        test_permission = PermissionFactory()
        client = app.test_client()
        test_data = {'name': test_permission.name}
        url = f"/api/permission"
        response = client.post(url, json=test_data)
        self.assertEqual(response.status_code, 201)
        permission = Permission.query.order_by(Permission.id).all()
        last_emp = permission[-1]
        db.session.delete(last_emp)
        db.session.commit()

    def test_get_permission_all(self):
        url = f"/api/permission"
        client = app.test_client()
        response = client.get(url)
        permission = Permission.query.order_by(Permission.id).all()
        self.assertEqual(len(response.json), len(permission))
