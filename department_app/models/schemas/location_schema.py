from pydantic import BaseModel, validator
from department_app.models.app_models import Location
from flask import request


class LocationModel(BaseModel):
    name: str

    @validator('name')
    def name_length(cls, v):
        location = Location.query.all()
        if len(v) > 100:
            raise ValueError('Name length too big!')
        if v in [x.name for x in location] and 'name' in request.json:
            raise ValueError('This location is already in use!')
        return v.title()
