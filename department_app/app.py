"""web app"""
import os
import logging

from flask_migrate import Migrate
from flasgger import Swagger
from flask import Flask

from department_app.database import db
from department_app.rest.permission import permission_api
from department_app.rest.department import department_api
from department_app.rest.location import location_api
from department_app.rest.employee import employee_api
from department_app.rest.address import address_api
from department_app.views.routes import frontend
from department_app.rest.skill import skill_api
from department_app.config import Config

logging.basicConfig(filename="app.log", level=logging.INFO)


def create_app():
    """Create app method"""

    app = Flask(__name__)
    app.config.from_object(os.environ.get('APP_SETTINGS', 'department_app.config.TestingConfig'))

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

    migrate = Migrate(app, db, directory=Config.MIGRATION_DIR)

    app.register_blueprint(department_api)
    app.register_blueprint(permission_api)
    app.register_blueprint(location_api)
    app.register_blueprint(employee_api)
    app.register_blueprint(address_api)
    app.register_blueprint(skill_api)
    app.register_blueprint(frontend)

    return app
