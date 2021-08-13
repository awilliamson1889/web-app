from pydantic import BaseModel, validator


class PermissionSchema(BaseModel):
    name: str

    @validator('name')
    def name_length(cls, v):
        # permission = Permission.query.all()
        if len(v) > 50:
            raise ValueError('Name length too big!')
        # if v in [x.name for x in permission] and 'name' in request.json:
        #     raise ValueError('This permission is already in use!')
        return v.title()