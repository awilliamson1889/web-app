from pydantic import BaseModel, validator
from flask import request
import math
import datetime
import re


class EmployeeSchema(BaseModel):
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
        return str(v).title()

    @validator('phone')
    def phone_check(cls, v):
        if not v.isdigit():
            raise ValueError('The number must contain only digits!')
        return v.title()

    @validator('email')
    def email_check(cls, v):
        regex = r'^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$'
        if not re.match(regex, v) and 'email' in request.json:
            raise ValueError('Check the correctness of the email!')
        return v.title()

    @validator('date_of_joining')
    def date_of_joining_check(cls, v):
        datetime.datetime.strptime(str(v), "%Y-%m-%d").date()
        return v.title()

    @validator('salary')
    def salary_check(cls, v):
        if v < 0:
            raise ValueError('Salary less then 0!')
        return v
