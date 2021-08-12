import factory
from department_app.models import LocationModel


class LocationFactory(factory.Factory):
    class Meta:
        model = LocationModel

    name = factory.Faker('country')


