import factory
from department_app.models import EmployeeModel


class EmployeeFactory(factory.Factory):
    class Meta:
        model = EmployeeModel

    name = factory.Faker('first_name')
    surname = factory.Faker('last_name')
    date_of_birth = '1999-01-01'
    salary = factory.Faker('pyint')
    email = factory.Faker('ascii_email')
    phone = factory.Faker('msisdn')
    date_of_joining = '1999-01-01'
    department = 1
    location = 1
    work_address = 1
    key_skill = 1
    permission = 1
