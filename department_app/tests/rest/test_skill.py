import unittest
from flask_fixtures import FixturesMixin

from department_app.app import create_app
from department_app.tests import SkillFactory
from department_app.database import db

app = create_app('TestingConfig')
app.app_context().push()


class TestApiSkill(unittest.TestCase, FixturesMixin):
    """Test skill api class"""

    fixtures = ['skill.yaml']

    app = app
    db = db

    def setUp(self):
        """setUp method"""
        self.app = app.test_client()

    def test_get_skill(self):
        """Api should return information about skill."""
        url = "/api/skill/1"
        response = self.app.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], 1)
        self.assertEqual(response.json['name'], 'Python')

    def test_get_skill_not_exist(self):
        """If skill doesnt exist Api should return error message"""
        url = f"/api/skill/999999999"
        response = self.app.get(url)
        message = f"Could not find skill with ID: {999999999}."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_skill_wrong_format1(self):
        """If skill id have wrong format, Api should return error message"""
        url = "/api/skill/one"
        response = self.app.get(url)
        message = "ID must be a number."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_skill_wrong_format2(self):
        """If skill id have wrong format, Api should return error message"""
        url = "/api/skill/-1"
        response = self.app.get(url)
        message = "ID must be a number."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_skill(self):
        """Api should update skill information"""
        url = "/api/skill/1"
        update_data = {'name': 'Rust'}
        response = self.app.put(url, json=update_data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], 'Rust')

    def test_put_skill_not_exist(self):
        """Api should update skill information"""
        url = "/api/skill/999999999"
        update_data = {'name': 'Rust'}
        response = self.app.put(url, json=update_data)
        message = f"Could not find skill with ID: {999999999}."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_skill_wrong_format1(self):
        """If skill id have wrong format, Api should return error message"""
        url = "/api/skill/one"
        response = self.app.put(url)
        message = "ID must be a number."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_skill_wrong_format2(self):
        """If skill id have wrong format, Api should return error message"""
        url = "/api/skill/-1"
        response = self.app.put(url)
        message = "ID must be a number."

        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_skill_wrong_name(self):
        """If skill name have wrong format, Api should return error message"""
        url = "/api/skill/1"
        update_data = {'name': 'Rust Rust Rust Rust Rust Rust'
                               'Rust Rust Rust Rust Rust Rust'
                               'Rust Rust Rust Rust Rust Rust'
                               'Rust Rust Rust Rust Rust Rust'
                               'Rust Rust Rust Rust Rust Rust'}
        response = self.app.put(url, json=update_data)
        message = "Exception: 1 validation error for SkillSchema\nname\n  Name length too big! (type=value_error)"

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], message)

    def test_post_skill(self):
        """Api should create new skill"""
        random_data = SkillFactory()
        post_data = {'name': random_data.name}
        url = "/api/skill"
        response = self.app.post(url, json=post_data)

        self.assertEqual(response.status_code, 201)

    def test_post_skill_wrong_name(self):
        """If skill name have wrong format, Api should return error message"""
        url = "/api/skill"
        post_data = {'name': 'Rust Rust Rust Rust Rust Rust'
                             'Rust Rust Rust Rust Rust Rust'
                             'Rust Rust Rust Rust Rust Rust'
                             'Rust Rust Rust Rust Rust Rust'
                             'Rust Rust Rust Rust Rust Rust'}
        response = self.app.post(url, json=post_data)
        message = "Exception: 1 validation error for SkillSchema\nname\n  Name length too big! (type=value_error)"

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], message)

    def test_get_skill_list(self):
        """Api should return all skill information"""
        url = f"/api/skill"
        response = self.app.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 4)
