from unittest.mock import patch
import unittest

from department_app.rest import Skill, SkillList
from department_app.tests import SkillFactory


class TestApiSkill(unittest.TestCase):
    """Test skill api class"""

    @patch('department_app.rest.skill.CRUDSkill.get_skill')
    def test_get_skill(self, mock_get_skill):
        """Api should return information about skill."""
        mock_get_skill.return_value = {'id': 100,
                                       'name': 'Some Skill'}
        response = Skill.get(100)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], 100)
        self.assertEqual(response.json['name'], 'Some Skill')

    @patch('department_app.rest.skill.CRUDSkill.update_skill')
    def test_put_skill(self, mock_update_skill):
        """Api should return information about skill."""
        mock_update_skill.return_value = {'id': 100,
                                          'name': 'Updated Skill'}
        response = Skill.put(100)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['id'], 100)
        self.assertEqual(response.json['name'], 'Updated Skill')

    @patch('department_app.rest.skill.CRUDSkill.create_skill')
    def test_post_skill(self, mock_create_skill):
        """Api should return information about skill."""
        mock_create_skill.return_value = {'id': 100,
                                          'name': 'New Skill'}
        response = SkillList.post()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['id'], 100)
        self.assertEqual(response.json['name'], 'New Skill')

    @patch('department_app.rest.skill.CRUDSkill.get_all_skill')
    def test_get_all_skill(self, mock_get_all_skill):
        """Api should return information about skills."""
        mock_get_all_skill.return_value = [
            {
                "skill_id": 1,
                "name": "Some Skill1"
            },
            {
                "skill_id": 2,
                "name": "Some Skill2"
            },
            {
                "skill_id": 3,
                "name": "Some Skill3"
            }]
        response = SkillList.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 3)
        self.assertEqual(response.json[0]['skill_id'], 1)
        self.assertEqual(response.json[0]['name'], 'Some Skill1')
