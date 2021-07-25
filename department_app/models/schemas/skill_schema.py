from pydantic import BaseModel, validator
from department_app.models.app_models import Skill
from flask import request


class SkillModel(BaseModel):
    name: str

    @validator('name')
    def name_length(cls, v):
        skill = Skill.query.all()
        if len(v) > 50:
            raise ValueError('Name length too big!')
        if v in [x.name for x in skill] and 'name' in request.json:
            raise ValueError('This skill is already in use!')
        return v.title()
