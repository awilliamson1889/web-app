from pydantic import BaseModel, validator
from flask import request
from department_app.models.app_models import Employee, Department, Skill, Address, Permission, Location
import math
import datetime
import re


class EmployeeModel(BaseModel):
    name: str
    surname: str
    date_of_birth: str
    salary: float
    email: str
    phone: str
    date_of_joining: str
    department: int
    location: int
    work_address: int
    key_skill: int
    permission: int

    @validator('name')
    def name_length(cls, v):
        if len(v) > 50:
            raise ValueError('Name length too big!')
        return v.title()

    @validator('surname')
    def surname_length(cls, v):
        if len(v) > 50:
            raise ValueError('Surname length too big!')
        return v.title()

    @validator('phone')
    def phone_length(cls, v):
        if len(v) > 13:
            raise ValueError('Phone length too big!')
        return v.title()

    @validator('date_of_birth')
    def date_of_birth_check(cls, v):
        age = (math.floor(
            (datetime.date.today() - datetime.datetime.strptime(str(v), "%Y-%m-%d").date()).days / 365))
        if age < 18 and 'date_of_birth' in request.json:
            raise ValueError('The employee cannot be under the age of 18!')
        return v.title()

    @validator('phone')
    def phone_check(cls, v):
        emp = Employee.query.all()
        if v in [x.phone for x in emp] and 'phone' in request.json:
            raise ValueError('This number is already in use!')
        if not v.isdigit():
            raise ValueError('The number must contain only digits!')
        return v.title()

    @validator('email')
    def email_check(cls, v):
        regex = r'\b[\w.-]+?@\w+?\.\w+?\b'
        emp = Employee.query.all()
        if v.lower() in [x.email.lower() for x in emp] and 'email' in request.json:
            raise ValueError('This email is already in use!')
        if not re.match(regex, v) and 'email' in request.json:
            raise ValueError('Check the correctness of the email!')
        return v.title()

    @validator('department')
    def department_check(cls, v):
        dep = Department.query.all()
        if v not in [x.id for x in dep]:
            raise ValueError('There is no such department! See the list of departments: .../swagger/#/Department32API')
        return v

    @validator('location')
    def location_check(cls, v):
        location = Location.query.all()
        if v not in [x.id for x in location]:
            raise ValueError('There is no such department! See the list of departments: .../swagger/#/Location32API')
        return v

    @validator('work_address')
    def work_address_check(cls, v):
        address = Address.query.all()
        if v not in [x.id for x in address]:
            raise ValueError('There is no such department! See the list of departments: .../swagger/#/Address32API')
        return v

    @validator('key_skill')
    def key_skill_check(cls, v):
        skill = Skill.query.all()
        if v not in [x.id for x in skill]:
            raise ValueError('There is no such department! See the list of departments: .../swagger/#/Skill32API')
        return v

    @validator('permission')
    def permission_check(cls, v):
        permission = Permission.query.all()
        if v not in [x.id for x in permission]:
            raise ValueError('There is no such department! See the list of departments: .../swagger/#/Permission32API')
        return v

    @validator('date_of_joining')
    def date_of_joining_check(cls, v):
        datetime.datetime.strptime(str(v), "%Y-%m-%d").date()
        return v.title()