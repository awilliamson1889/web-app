import factory
from department_app.models.app_models import Location


class LocationFactory(factory.Factory):
    class Meta:
        model = Location

    name = factory.Faker('country')


