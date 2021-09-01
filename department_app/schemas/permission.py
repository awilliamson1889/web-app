from pydantic import BaseModel, validator


class PermissionSchema(BaseModel):
    name: str

    @validator('name')
    def name_length(cls, v):
        if len(v) > 50:
            raise ValueError('Name length too big!')
        return v.title()
