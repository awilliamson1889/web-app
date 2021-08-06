"""Address schema"""
from pydantic import BaseModel, validator
from department_app.models.app_models import Address
from flask import request


class AddressSchema(BaseModel):
    """Address schema class"""
    name: str

    @validator('name')
    def name_length(cls, v):
        """Address name validation"""
        address = Address.query.all()
        if len(v) > 100:
            raise ValueError('Name length too big!')
        if v in [x.name for x in address] and 'name' in request.json:
            raise ValueError('This address is already in use!')
        return v.title()
