"""Skill CRUD"""
from flask import request
from department_app.models.app_models import db, Skill


class CRUDSkill:
    """Employee CRUD class"""
    @staticmethod
    def get_all_skill():
        """Get skill func"""
        skill_list = []
        skills = Skill.query.all()
        for skill in skills:
            skill_info = {'name': skill.name, 'skill_id': skill.id}
            skill_list.append(skill_info)
        return tuple(skill_list)

    @staticmethod
    def create_skill():
        """Create department func"""
        form_data = request.form
        skill = Skill(name=form_data['name'])
        db.session.add(skill)
        db.session.commit()
