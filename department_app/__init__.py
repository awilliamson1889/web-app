"""web app"""
import os
from flask import Flask
from flask_migrate import Migrate
from flasgger import Swagger
from department_app.models.app_models import db

MIGRATION_DIR = os.path.join('department_app/migrations')


def create_app(config_name):
    """Create app method"""
    app = Flask(__name__)
    app.config.from_object('config.' + config_name)

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

    db.init_app(app)
    with app.app_context():
        db.create_all()
        # db.session.commit()

    migrate = Migrate(app, db, directory=MIGRATION_DIR)

    import department_app.views.routes
    import department_app.rest.employee_api
    import department_app.rest.department_api
    import department_app.rest.location_api
    import department_app.rest.permission_api
    import department_app.rest.skill_api
    import department_app.rest.address_api
    from department_app.models.app_models import Employee, Department, Permission, Address, Location, Skill

    app.register_blueprint(department_app.views.routes.frontend)
    app.register_blueprint(department_app.rest.employee_api.employee_api)
    app.register_blueprint(department_app.rest.department_api.department_api)
    app.register_blueprint(department_app.rest.location_api.location_api)
    app.register_blueprint(department_app.rest.permission_api.permission_api)
    app.register_blueprint(department_app.rest.skill_api.skill_api)
    app.register_blueprint(department_app.rest.address_api.address_api)

    return app
