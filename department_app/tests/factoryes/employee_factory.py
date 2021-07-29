import factory
import random
from department_app import create_app
from department_app.models.app_models import Employee, Department, Permission, Address, Location, Skill

app = create_app('Test')
app.app_context().push()

department = Department.query.order_by(Department.id).all()
department_list = [department_id.id for department_id in department]

permission = Permission.query.order_by(Permission.id).all()
permission_list = [permission_id.id for permission_id in permission]

address = Address.query.order_by(Address.id).all()
address_list = [address_id.id for address_id in address]

location = Location.query.order_by(Location.id).all()
location_list = [location_id.id for location_id in location]

skill = Skill.query.order_by(Skill.id).all()
skill_list = [skill_id.id for skill_id in skill]


class EmployeeFactory(factory.Factory):
    class Meta:
        model = Employee

    name = factory.Faker('first_name')
    surname = factory.Faker('last_name')
    date_of_birth = '01-01-1999'
    salary = factory.Faker('pyint')
    email = factory.Faker('ascii_email')
    phone = factory.Faker('msisdn')
    date_of_joining = '01-01-1999'
    department = random.choice(department_list)
    location = random.choice(location_list)
    work_address = random.choice(address_list)
    key_skill = random.choice(skill_list)
    permission = random.choice(permission_list)
