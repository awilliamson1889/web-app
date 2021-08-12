import factory
from department_app.models import DepartmentModel


class DepartmentFactory(factory.Factory):
    class Meta:
        model = DepartmentModel

    name = factory.Faker('job')
    manager = factory.Faker('first_name')
    date_of_creation = '2021-01-01'
