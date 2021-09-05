"""Department CRUD"""
import logging
from sqlalchemy.exc import IntegrityError

from department_app.models import DepartmentModel, EmployeeModel
from department_app.database import db


class CRUDDepartment:
    """Department CRUD class"""
    @staticmethod
    def get(department_id):
        """Get department func"""
        logging.info("Get department method called with parameters: id=%s", department_id)

        department_query = DepartmentModel.query.filter_by(id=department_id).all()
        if not department_query:
            return None
        for department in department_query:
            employee = EmployeeModel.query.filter_by(department=department.id).all()
            department_info = {'name': department.name,
                               'manager': department.manager,
                               'date_of_creation': department.date_of_creation,
                               'employees': len(EmployeeModel.query.filter_by(department=department.id).all()),
                               'department_avg_salary': sum([x.salary for x in employee]),
                               'department_id': department.id}
            return department_info

    @staticmethod
    def update(department_id, name, date_of_creation, manager):
        """Update department func"""
        logging.info("Update location method called with parameters: id=%s, name=%s, date_of_creation=%s, manager=%s.",
                     department_id, name, date_of_creation, manager)

        try:
            result = DepartmentModel.query.where(DepartmentModel.id == department_id). \
                update({DepartmentModel.name: name,
                        DepartmentModel.date_of_creation: date_of_creation,
                        DepartmentModel.manager: manager})
            db.session.commit()
        except IntegrityError:
            logging.info("Department with name=%s already exist.", name)
            raise
        return bool(result)

    @staticmethod
    def get_department_list(filters=None):
        """Get department func"""
        department_list = []
        if filters:
            departments = DepartmentModel.query.filter(DepartmentModel.name.
                                                       like(('%' + str(filters.get('department_name')) + '%'))).all()
        else:
            departments = DepartmentModel.query.all()
        if len(departments) > 0:
            for department in departments:
                employee = EmployeeModel.query.filter_by(department=department.id).all()
                department_info = {'name': department.name,
                                   'manager': department.manager,
                                   'date_of_creation': department.date_of_creation,
                                   'employees': len(EmployeeModel.query.filter_by(department=department.id).all()),
                                   'department_avg_salary': sum([x.salary for x in employee]),
                                   'department_id': department.id}
                department_list.append(department_info)
            return tuple(department_list)
        return department_list

    @staticmethod
    def create(name, date_of_creation, manager):
        """Create department func"""
        logging.info("Create location method called with parameters: name=%s, date_of_creation=%s, manager=%s.",
                     name, date_of_creation, manager)

        department = DepartmentModel(name=name, date_of_creation=date_of_creation, manager=manager)

        try:
            db.session.add(department)
            db.session.commit()
        except IntegrityError:
            logging.info("Department with name=%s already exist.", name)
            raise
        return department
