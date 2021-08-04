import factory
from department_app.models.app_models import Permission


class PermissionFactory(factory.Factory):
    class Meta:
        model = Permission

    name = factory.Faker('first_name')


