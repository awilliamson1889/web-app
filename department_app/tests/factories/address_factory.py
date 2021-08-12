import factory
from department_app.models import AddressModel


class AddressFactory(factory.Factory):
    class Meta:
        model = AddressModel

    name = factory.Faker('address')


