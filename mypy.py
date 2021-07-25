from department_app.models.app_models import db, Department, Permission, Address, Location, Skill
from department_app import create_app
import random

app = create_app('Test')
app.app_context().push()

department = Department(name="test_department_name___",
                        manager="test_department_manager__",
                        date_of_creation="2021-01-01")

permission = Permission(name="test_permission__")

address = Address(name="test_address__")

location = Location(name="test_location__")

skill = Skill(name="test_skill__")

db.session.add(department)
db.session.add(permission)
db.session.add(address)
db.session.add(location)
db.session.add(skill)
db.session.commit()
