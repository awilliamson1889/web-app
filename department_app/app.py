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
from department_app.rest.skill import skill_api
from department_app.config import Config
from department_app.views import AddAddress, AddDepartment, AddLocation, AddEmployee, AddSkill, AddPermission, \
    DeleteEmployee, DepartmentPage, DepartmentsPage, EmployeePage, ManageDepartment, ManageEmployee, SearchEmployee,\
    UpdateDepartment, UpdateEmployee, DeleteDepartment, MainPage

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
    # app.register_blueprint(frontend)

    app.add_url_rule('/', view_func=MainPage.as_view('main_page'))
    app.add_url_rule('/add/address', view_func=AddAddress.as_view('add_address'))
    app.add_url_rule('/add/department', view_func=AddDepartment.as_view('add_department'))
    app.add_url_rule('/add/employee', view_func=AddEmployee.as_view('add_employee'))
    app.add_url_rule('/add/location', view_func=AddLocation.as_view('add_location'))
    app.add_url_rule('/add/permission', view_func=AddPermission.as_view('add_permission'))
    app.add_url_rule('/add/skill', view_func=AddSkill.as_view('add_skill'))
    app.add_url_rule('/delete-employee/<string:employee_id>', view_func=DeleteEmployee.as_view('delete_employee'))
    app.add_url_rule('/delete-department/<string:department_id>',
                     view_func=DeleteDepartment.as_view('delete_department'))
    app.add_url_rule('/departments', view_func=DepartmentsPage.as_view('departments_page'))
    app.add_url_rule('/department/<string:department_id>', view_func=DepartmentPage.as_view('department_page'))
    app.add_url_rule('/employee/<string:employee_id>', view_func=EmployeePage.as_view('employee_page'))
    app.add_url_rule('/manage/employee', view_func=ManageEmployee.as_view('manage_employee_page'))
    app.add_url_rule('/manage/department', view_func=ManageDepartment.as_view('manage_department_page'))
    app.add_url_rule('/search/employee', view_func=SearchEmployee.as_view('search_employee_page'))
    app.add_url_rule('/update-employee/<string:employee_id>', view_func=UpdateEmployee.as_view('update_employee'))
    app.add_url_rule('/update-department/<string:department_id>',
                     view_func=UpdateDepartment.as_view('update_department'))

    return app
