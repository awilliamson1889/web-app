from pydantic import BaseModel, validator


class LocationSchema(BaseModel):
    name: str

    @validator('name')
    def name_length(cls, v):
        if len(v) > 100:
            raise ValueError('Name length too big!')
        return v.title()
