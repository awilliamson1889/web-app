import factory
from department_app.models import SkillModel


class SkillFactory(factory.Factory):
    class Meta:
        model = SkillModel

    name = factory.Faker('first_name')
