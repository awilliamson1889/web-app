import factory
from department_app.models.app_models import Address


class AddressFactory(factory.Factory):
    class Meta:
        model = Address

    name = factory.Faker('address')


