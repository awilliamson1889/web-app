"""Skill CRUD"""
from sqlalchemy.exc import IntegrityError
from pydantic import ValidationError
from flask_restful import abort
from flask import request

from department_app.schemas import SkillSchema
from department_app.models import SkillModel
from department_app.database import db
from .service import check_id_format


class CRUDSkill:
    """Employee CRUD class"""
    @staticmethod
    def get_skill(skill_id):
        """Get skill func"""
        check_id_format(skill_id)
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
    def update_skill(skill_id):
        """update skill func"""
        skill = CRUDSkill.get_skill(skill_id)

        skill_data = {'name': skill.name}

        skill_json = request.json
        skill_data.update(skill_json)

        try:
            SkillSchema(**skill_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        skill.name = skill_data['name']

        try:
            db.session.commit()
        except IntegrityError as exception:
            abort(404, message=f"Exception: {exception}")
        return skill

    @staticmethod
    def create_skill(form=None):
        """Create department func"""
        if form:
            skill_data = {'name': form.name.data}
        else:
            skill_data = {'name': request.json['name']}

        skill = SkillModel(**skill_data)

        try:
            SkillSchema(**skill_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        try:
            db.session.add(skill)
            db.session.commit()
        except IntegrityError as exception:
            abort(404, message=f"Exception: {exception}")

        return skill
