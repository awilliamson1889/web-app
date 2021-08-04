"""web app"""
import os
from flask import Flask
from flask_migrate import Migrate
from flasgger import Swagger
from department_app.models.app_models import db

MIGRATION_DIR = os.path.join('department_app/migrations')


def create_app(test_config=None):
    """Create app method"""

    app = Flask(__name__)
    # app.config['SWAGGER'] = {"title": "DevSwagger-UI", "uiversion": 2}
    # app.config['DEVELOPMENT'] = True
    # app.config['DEBUG'] = True
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/flask_app'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_app.db'
    if test_config is None or test_config == 'Dev':
        app.config.from_object("config.DevelopmentConfig")
    elif test_config == 'Prod':
        app.config.from_object("config.ProductionConfig")
    elif test_config == 'Test':
        app.config.from_object("config.TestingConfig")

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
