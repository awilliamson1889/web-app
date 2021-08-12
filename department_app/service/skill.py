"""Skill CRUD"""
from sqlalchemy.exc import IntegrityError
from flask import request
from flask_restful import abort
from department_app.models import SkillModel
from department_app.database import db


class CRUDSkill:
    """Employee CRUD class"""
    @staticmethod
    def get_skill(skill_id):
        """Get skill func"""
        if not str(skill_id).isdigit():
            abort(404, message="ID must be a number.")
        skill = SkillModel.query.filter_by(id=skill_id).first()
        if not skill:
            abort(404, message=f"Could not find skill with ID: {skill_id}.")
        return skill

    @staticmethod
    def get_all_skill():
        """Get skill func"""
        skill_list = []
        skills = SkillModel.query.all()
        for skill in skills:
            skill_info = {'name': skill.name, 'skill_id': skill.id}
            skill_list.append(skill_info)
        return tuple(skill_list)

    @staticmethod
    def update_skill(skill_id, json):
        """update skill func"""
        skill = SkillModel.query.filter_by(id=skill_id).first()
        skill.name = json['name']

        try:
            db.session.commit()
        except IntegrityError as exception:
            abort(404, message=f"Exception: {exception}")
        return skill

    @staticmethod
    def create_skill(form=None):
        """Create department func"""
        if form:
            skill = SkillModel(name=form.name.data)
        else:
            skill = SkillModel(name=request.json['name'])

        try:
            db.session.add(skill)
            db.session.commit()
        except IntegrityError as exception:
            abort(404, message=f"Exception: {exception}")
