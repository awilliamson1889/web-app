"""Address schema"""
from pydantic import BaseModel, validator


class AddressModel(BaseModel):
    """Address schema class"""
    name: str

    @validator('name')
    def name_length(cls, v):
        """Address name validation"""
        if len(v) > 100:
            raise ValueError('Name length too big!')
        return v.title()
