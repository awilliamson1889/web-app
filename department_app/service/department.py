"""Department CRUD"""
from sqlalchemy.exc import IntegrityError
from flask_restful import abort
from flask import request
from department_app.models import DepartmentModel, EmployeeModel
from department_app.database import db


class CRUDDepartment:
    """Department CRUD class"""
    @staticmethod
    def delete_department(department_id):
        """Delete department func"""
        DepartmentModel.query.filter_by(id=department_id).delete()
        db.session.commit()

    @staticmethod
    def create_department(form=None):
        """Create department func"""
        if form:
            department = DepartmentModel(name=form.name.data, date_of_creation=form.date_of_creation.data,
                                         manager=form.manager.data)
        else:
            department = DepartmentModel(name=request.json['name'], date_of_creation=request.json['date_of_creation'],
                                         manager=request.json['manager'])

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
        if not str(department_id).isdigit():
            abort(404, message="ID must be a number.")
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
    def update_department(department_id, json):
        """Update department func"""
        department = DepartmentModel.query.filter_by(id=department_id).first()

        department.name = json['name']
        department.manager = json['manager']
        department.date_of_creation = json['date_of_creation']

        try:
            db.session.commit()
        except IntegrityError as exception:
            abort(404, message=f"Exception: {exception}")
        return department
