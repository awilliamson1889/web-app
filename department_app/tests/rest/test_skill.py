from unittest.mock import patch
import unittest

from department_app.rest import Skill, SkillList
from department_app.app import create_app

app = create_app()
app.app_context().push()


class TestApiSkill(unittest.TestCase):
    """Test skill api class"""
    update_success_msg = "Data successful updated."
    update_fail_msg = "Skill not updated."
    wrong_id_format_msg = "Invalid ID format!"
    wrong_json_msg = "Wrong JSON fields names."
    not_valid_json_msg = "JSON is not valid."

    wrong_json = {"name_field": "Some Skill1"}

    post_valid_data = {"name": "POST SKILL"}
    put_valid_data = {"name": "PUT SKILL"}
    post_invalid_data = {"name": "Some Skill1 Some Skill1 Some Skill1 Some Skill1 Some Skill1 Some Skill1"
                                 "Some Skill1 Some Skill1 Some Skill1 Some Skill1 Some Skill1 Some Skill1"
                                 "Some Skill1 Some Skill1 Some Skill1 Some Skill1 Some Skill1 Some Skill1"
                                 "Some Skill1 Some Skill1 Some Skill1 Some Skill1 Some Skill1 Some Skill1"}

    valid_test_data = [
            {
                "id": 1,
                "name": "Some Skill1"
            },
            {
                "id": 2,
                "name": "Some Skill2"
            },
            {
                "id": 3,
                "name": "Some Skill3"}]

    @patch('department_app.rest.skill.CRUDSkill.get')
    def test_get_skill(self, mock_get_skill):
        """Api should return information about skill."""
        mock_get_skill.return_value = self.valid_test_data[0]
        response = Skill.get(1)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['id'], self.valid_test_data[0]['id'])
        self.assertEqual(response.json['name'], self.valid_test_data[0]['name'])

    @patch('department_app.rest.skill.abort')
    def test_get_skill_wrong_id_case1(self, mock_abort):
        """Api should return information about skill."""
        Skill.get('one')

        mock_abort.assert_called_once_with(404, message=self.wrong_id_format_msg)

    @patch('department_app.rest.skill.abort')
    def test_get_skill_wrong_id_case2(self, mock_abort):
        """Api should return information about skill."""
        Skill.get(-1)

        mock_abort.assert_called_once_with(404, message=self.wrong_id_format_msg)

    @patch('department_app.rest.skill.abort')
    def test_get_skill_wrong_id_case3(self, mock_abort):
        """Api should return information about skill."""
        Skill.get(1.0)

        mock_abort.assert_called_once_with(404, message=self.wrong_id_format_msg)

    @patch('department_app.rest.skill.abort')
    @patch('department_app.rest.skill.CRUDSkill.get')
    def test_get_skill_not_exist(self, mock_get_skill, mock_abort):
        """Api should return information about skill."""
        mock_get_skill.return_value = None
        Skill.get(1)

        mock_abort.assert_called_once_with(404, message="No such skill with ID=1")

    @patch('department_app.rest.skill.CRUDSkill.update')
    @patch('department_app.rest.skill.Skill.get_json')
    def test_put_skill_success(self, mok_get_json, mock_update):
        """Api should return information about skill."""
        mok_get_json.return_value = self.put_valid_data
        mock_update.return_value = True
        response = Skill.put(1)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], self.update_success_msg)

    @patch('department_app.rest.skill.abort')
    @patch('department_app.rest.skill.CRUDSkill.update')
    @patch('department_app.rest.skill.Skill.get_json')
    def test_put_skill_fail(self, mok_get_json, mock_update, mock_abort):
        """Api should return information about skill."""
        mok_get_json.return_value = self.put_valid_data
        mock_update.return_value = False
        Skill.put(1)

        mock_abort.assert_called_once_with(404, message=self.update_fail_msg)

    @patch('department_app.rest.skill.abort')
    @patch('department_app.rest.skill.Skill.get_json')
    def test_put_skill_not_valid(self, mok_get_json, mock_abort):
        """Api should return information about skill."""
        mok_get_json.return_value = self.post_invalid_data
        Skill.put(1)

        mock_abort.assert_called_once_with(404, message=self.not_valid_json_msg)

    @patch('department_app.rest.skill.abort')
    @patch('department_app.rest.skill.Skill.get_json')
    def test_put_skill_wrong_json(self, mok_get_json, mock_abort):
        """Api should return information about skill."""
        mok_get_json.return_value = False
        Skill.put(1)

        mock_abort.assert_called_once_with(404, message=self.wrong_json_msg)

    @patch('department_app.rest.skill.Skill.get_json')
    @patch('department_app.rest.skill.CRUDSkill.create')
    def test_post_skill(self, mock_create_skill, mok_get_json):
        """Api should return information about skill."""
        mok_get_json.return_value = self.post_valid_data
        mock_create_skill.return_value = {'id': 1,
                                            'name': self.post_valid_data['name']}
        response = SkillList.post()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['id'], 1)
        self.assertEqual(response.json['name'], self.post_valid_data['name'])

    @patch('department_app.rest.skill.abort')
    @patch('department_app.rest.skill.Skill.get_json')
    def test_post_skill_not_valid(self, mok_get_json, mok_abort):
        """Api should return information about skill."""
        mok_get_json.return_value = self.post_invalid_data

        SkillList.post()

        mok_abort.assert_called_once_with(404, message=self.not_valid_json_msg)

    @patch('department_app.rest.skill.abort')
    @patch('department_app.rest.skill.Skill.get_json')
    def test_post_skill_wrong_json(self, mok_get_json, mock_abort):
        """Api should return information about skill."""
        mok_get_json.return_value = False

        SkillList.post()

        mock_abort.assert_called_once_with(404, message=self.wrong_json_msg)

    @patch('department_app.rest.skill.CRUDSkill.get_skill_list')
    def test_get_all_skill(self, mock_get_all_skill):
        """Api should return information about skill."""
        mock_get_all_skill.return_value = self.valid_test_data
        response = SkillList.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), len(self.valid_test_data))
        self.assertEqual(response.json[0]['id'], self.valid_test_data[0]['id'])
        self.assertEqual(response.json[0]['name'], self.valid_test_data[0]['name'])

    @patch('department_app.rest.skill.CRUDSkill.get_skill_list')
    def test_get_all_skill_empty(self, mock_get_all_skill):
        """Api should return information about skill."""
        mock_get_all_skill.return_value = []
        response = SkillList.get()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 0)
