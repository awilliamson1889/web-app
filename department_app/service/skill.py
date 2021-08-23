"""Skill CRUD"""
import logging
from sqlalchemy.exc import IntegrityError

from department_app.models import SkillModel
from department_app.database import db


class CRUDSkill:
    """Skill CRUD class"""
    @staticmethod
    def get(skill_id):
        """Get skill func"""
        logging.info("Get skill method called with parameters: id=%s", skill_id)

        return SkillModel.query.filter_by(id=skill_id).first()

    @staticmethod
    def update(skill_id, name):
        """update skill func"""
        logging.info("Update skill method called with parameters: id=%s, name=%s.", skill_id, name)

        try:
            result = SkillModel.query.where(SkillModel.id == skill_id). \
                update({SkillModel.name: name})
            db.session.commit()
        except IntegrityError as exception:
            logging.info("Skill with name=%s already exist.", name)
            raise exception
        return bool(result)

    @staticmethod
    def get_skill_list():
        """Get skill func"""
        skills = SkillModel.query.all()

        if len(skills) > 0:
            return tuple(({'name': skill.name,
                           'id': skill.id} for skill in skills))
        return []

    @staticmethod
    def create(name):
        """Create skill func"""
        logging.info("Create skill method called with parameters: name=%s.", name)

        skill = SkillModel(name=name)

        try:
            db.session.add(skill)
            db.session.commit()
        except IntegrityError as exception:
            logging.info("Skill with name=%s already exist.", name)
            raise exception
        return skill
