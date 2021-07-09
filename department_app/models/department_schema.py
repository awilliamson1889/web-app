from pydantic import BaseModel, validator
from department_app.models.app_models import Department
from flask import request
import datetime


class DepartmentModel(BaseModel):
    id: int
    name: str
    manager: str
    date_of_creation: str

    @validator('name')
    def name_length(cls, v):
        if len(v) > 100:
            raise ValueError('Name length too big!')
        return v.title()

    @validator('date_of_creation')
    def date_of_birth_check(cls, v):
        datetime.datetime.strptime(str(v), "%Y-%m-%d").date()
        return v.title()

    @validator('name')
    def department_name_check(cls, v):
        dep = Department.query.all()
        if v.lower() in [x.name.lower() for x in dep]:
            raise ValueError('This name is already in use!')
        return v.title()

    @validator('manager')
    def department_manager_check(cls, v):
        dep = Department.query.all()
        if v in [x.manager for x in dep]:
            raise ValueError('This manager is already in use!')
        return v.title()
