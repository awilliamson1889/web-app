"""web app"""
import os
from flask import Flask
from flask_migrate import Migrate
from flasgger import Swagger
from department_app.database import db


MIGRATION_DIR = os.path.join('department_app/migrations')


def create_app(config='TestingConfig'):
    """Create app method"""

    app = Flask(__name__)
    app.config.from_object("config." + config)

    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "apiscpec_1",
                "route": "/apiscpec_1.json",
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/swagger/",
    }

    swagger = Swagger(app, config=swagger_config)

    migrate = Migrate(app, db, directory=MIGRATION_DIR)

    from department_app.views.routes import frontend
    app.register_blueprint(frontend)

    from department_app.rest.employee import employee_api
    app.register_blueprint(employee_api)

    from department_app.rest.department import department_api
    app.register_blueprint(department_api)

    from department_app.rest.location import location_api
    app.register_blueprint(location_api)

    from department_app.rest.permission import permission_api
    app.register_blueprint(permission_api)

    from department_app.rest.skill import skill_api
    app.register_blueprint(skill_api)

    from department_app.rest.address import address_api
    app.register_blueprint(address_api)

    from department_app.models import EmployeeModel, DepartmentModel, PermissionModel,\
        AddressModel, LocationModel, SkillModel

    return app
