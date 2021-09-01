import factory
from department_app.models import PermissionModel


class PermissionFactory(factory.Factory):
    class Meta:
        model = PermissionModel

    name = factory.Faker('first_name')


