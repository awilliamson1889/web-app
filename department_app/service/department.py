"""Department CRUD"""
import logging
from sqlalchemy.exc import IntegrityError

from department_app.models import DepartmentModel
from department_app.utilites import Department
from department_app.database import db


class CRUDDepartment:
    """Department CRUD class"""
    @staticmethod
    def get(department_id) -> Department:
        """Get department func"""
        logging.info("Get department method called with parameters: id=%s", department_id)

        department_query = DepartmentModel.query.get(department_id)
        department = Department.convert_db_to_entity(department_query)
        return department

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
    def get_department_list(filters=None) -> tuple:
        """Get department func"""
        if filters:
            departments = DepartmentModel.query.filter(DepartmentModel.name.
                                                       like(('%' + str(filters.get('department_name')) + '%'))).all()
        else:
            departments = DepartmentModel.query.all()
        if len(departments) > 0:
            department_list = [Department.convert_db_to_entity(dep) for dep in departments]
            return tuple(department_list)
        return tuple()

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
