"""Department CRUD"""
from sqlalchemy.exc import IntegrityError
from pydantic import ValidationError
from flask_restful import abort
from flask import request

from department_app.models import DepartmentModel, EmployeeModel
from department_app.schemas import DepartmentSchema
from department_app.database import db
from .service import check_id_format


class CRUDDepartment:
    """Department CRUD class"""

    @staticmethod
    def create_department(form=None):
        """Create department func"""
        if form:
            department_data = {'name': form.name.data, 'manager': form.manager.data,
                               'date_of_creation': form.date_of_creation.data}
            department = DepartmentModel(**department_data)
        else:
            department_data = {'name': request.json['name'], 'manager': request.json['manager'],
                               'date_of_creation': request.json['date_of_creation']}
            department = DepartmentModel(**department_data)

        try:
            DepartmentSchema(**department_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        try:
            db.session.add(department)
            db.session.commit()
        except IntegrityError as exception:
            abort(404, message=f"Exception: {exception}")

    @staticmethod
    def get_all_department(department_filter=None):
        """Get department func"""
        department_list = []
        if department_filter:
            departments = DepartmentModel.query.filter(DepartmentModel.name.like(str('%' + department_filter + '%')))
        else:
            departments = DepartmentModel.query.all()
        for department in departments:
            employee = EmployeeModel.query.filter_by(department=department.id).all()
            department_info = {'name': department.name,
                               'manager': department.manager,
                               'date_of_creation': department.date_of_creation,
                               'emp_count': len(EmployeeModel.query.filter_by(department=department.id).all()),
                               'dep_salary': sum([x.salary for x in employee]),
                               'dep_id': department.id}
            department_list.append(department_info)
        return tuple(department_list)

    @staticmethod
    def get_department(department_id):
        """Get department func"""
        check_id_format(department_id)

        department_query = DepartmentModel.query.filter_by(id=department_id).all()
        if not department_query:
            abort(404, message=f"Could not find department with ID: {department_id}.")
        else:
            for department in department_query:
                department_info = {'name': department.name,
                                   'manager': department.manager,
                                   'date_of_creation': department.date_of_creation,
                                   'emp_count': len(EmployeeModel.query.filter_by(department=department.id).all()),
                                   'dep_id': department.id}
                return department_info
        return False

    @staticmethod
    def update_department(department_id):
        """Update department func"""
        check_id_format(department_id)

        department = DepartmentModel.query.filter_by(id=department_id).first()
        if not department:
            abort(404, message=f"Could not find department with ID: {department_id}.")

        department_data = {'name': department.name, 'date_of_creation': department.date_of_creation,
                           'manager': department.manager}

        department_json = request.json
        department_data.update(department_json)

        try:
            DepartmentSchema(**department_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        department.name = department_data['name']
        department.manager = department_data['manager']
        department.date_of_creation = department_data['date_of_creation']

        try:
            db.session.commit()
        except IntegrityError as exception:
            abort(404, message=f"Exception: {exception}")
        return department
