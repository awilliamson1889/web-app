import unittest
from department_app import create_app
from department_app.service.skill import CRUDSkill
from department_app.models.app_models import Skill

app = create_app('Test')
app.app_context().push()


class TestSkillService(unittest.TestCase):
    """ doc str """
    def test_get_all_skill_method(self):
        skill_query = Skill.query.all()
        skills = CRUDSkill.get_all_skill()
        skills_len = len(skill_query)

        self.assertEqual(skills_len, len(skills))
