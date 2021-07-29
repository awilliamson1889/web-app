import factory
from department_app.models.app_models import Skill


class SkillFactory(factory.Factory):
    class Meta:
        model = Skill

    name = factory.Faker('first_name')
