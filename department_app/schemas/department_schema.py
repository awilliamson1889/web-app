"""Department schema"""
from pydantic import BaseModel, validator
from department_app.models.app_models import Department
from flask import request
import datetime


class DepartmentSchema(BaseModel):
    """Department schema class"""
    name: str
    manager: str
    date_of_creation: str

    @validator('name')
    def name_length(cls, v):
        """Name length validator"""
        dep = Department.query.all()
        if len(v) > 100:
            raise ValueError('Name length too big!')
        if v in [x.name for x in dep] and 'name' in request.json:
            raise ValueError('This department is already in use!')
        return v.title()

    @validator('date_of_creation')
    def date_of_creation_check(cls, v):
        """Date of creation validator"""
        datetime.datetime.strptime(str(v), "%Y-%m-%d").date()
        return str(v).title()

    @validator('manager')
    def department_manager_name_check(cls, v):
        """Department manager name validator"""
        if len(v) > 100 and 'manager' in request.json:
            raise ValueError('Manager name length too big!')
        return v.title()
