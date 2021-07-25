import unittest
from department_app import create_app
from department_app.models.app_models import db, Skill
from department_app.models.factoryes.skill_factory import SkillFactory


app = create_app('Test')
app.app_context().push()


class TestApiSkill(unittest.TestCase):
    """ doc str """
    def setUp(self):
        """ doc str """
        self.app = app.test_client()
        test_skill = SkillFactory()
        test_data = {'name': test_skill.name}
        skill = Skill(**test_data)
        db.session.add(skill)
        db.session.commit()
        db.create_all()

    def tearDown(self):
        skill = Skill.query.order_by(Skill.id).all()
        db.session.delete(skill[-1])
        db.session.commit()

    def test_get_skill(self):
        skill = Skill.query.order_by(Skill.id).all()
        last_skill = skill[-1]
        url = f"/api/skill/{last_skill.id}"
        client = app.test_client()
        response = client.get(url)

        self.assertEqual(200, response.status_code)
        self.assertEqual(last_skill.id, response.json['id'])
        self.assertEqual(last_skill.name, response.json['name'])

    def test_get_skill_not_exist(self):
        skill_id = 999999999
        client = app.test_client()
        url = f"/api/skill/{skill_id}"
        message = f"Could not find skill with ID: {skill_id}."
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_str_id_format(self):
        skill_id = "one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/skill/{skill_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_negative_num_id_format(self):
        skill_id = -1
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/skill/{skill_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_str_num_id_format(self):
        skill_id = "1one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/skill/{skill_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_get_float_num_id_format(self):
        skill_id = 1.0
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/skill/{skill_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_skill(self):
        skill = Skill.query.order_by(Skill.id).all()
        client = app.test_client()
        last_skill = skill[-1]
        update_test_data = {'name': 'update_test_skill'}
        url = f"/api/skill/{last_skill.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(201, response.status_code)
        self.assertEqual(last_skill.id, response.json['id'])
        self.assertEqual(update_test_data['name'], response.json['name'])

    def test_put_skill_not_exist(self):
        skill_id = 999999999
        client = app.test_client()
        url = f"/api/skill/{skill_id}"
        message = f"Could not find skill with ID: {skill_id}."
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_str_id_format(self):
        skill_id = "one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/skill/{skill_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_negative_num_id_format(self):
        skill_id = -1
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/skill/{skill_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_str_num_id_format(self):
        skill_id = "1one"
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/skill/{skill_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_float_num_id_format(self):
        skill_id = 1.0
        client = app.test_client()
        message = "ID must be a number."
        url = f"/api/skill/{skill_id}"
        response = client.put(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_big_skill_name(self):
        skill = Skill.query.order_by(Skill.id).all()
        last_skill = skill[-1]
        client = app.test_client()
        update_test_data = {'name': 'test_very_big_skill_test_very_big_skill_test_very_big_skill_test_very_big_skill_'
                                    'test_very_big_skill_test_very_big_skill_test_very_big_skill_test_very_big_skill'}
        message = "Exception: 1 validation error for SkillModel\nname\n  Name length too big! (type=value_error)"
        url = f"/api/skill/{last_skill.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_put_skill_already_exist(self):
        skill = Skill.query.order_by(Skill.id).all()
        client = app.test_client()
        last_skill = skill[-1]
        update_test_data = {'name': last_skill.name}
        message = "Exception: 1 validation error for SkillModel\n" \
                  "name\n  This skill is already in use! (type=value_error)"
        url = f"/api/skill/{last_skill.id}"
        response = client.put(url, json=update_test_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(message, response.json['message'])

    def test_post_skill(self):
        test_skill = SkillFactory()
        client = app.test_client()
        test_data = {'name': test_skill.name}
        url = f"/api/skill"
        response = client.post(url, json=test_data)
        self.assertEqual(response.status_code, 201)
        skill = Skill.query.order_by(Skill.id).all()
        last_skill = skill[-1]
        db.session.delete(last_skill)
        db.session.commit()

    def test_get_skill_all(self):
        url = f"/api/skill"
        client = app.test_client()
        response = client.get(url)
        skill = Skill.query.order_by(Skill.id).all()
        self.assertEqual(len(response.json), len(skill))
