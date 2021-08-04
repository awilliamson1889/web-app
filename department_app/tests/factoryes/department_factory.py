import factory
from department_app.models.app_models import Department


class DepartmentFactory(factory.Factory):
    class Meta:
        model = Department

    name = factory.Faker('job')
    manager = factory.Faker('first_name')
    date_of_creation = '01-01-2021'
