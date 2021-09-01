"""Employee CRUD"""
import logging
from sqlalchemy.exc import IntegrityError

from department_app.models import DepartmentModel, PermissionModel, AddressModel, LocationModel,\
    SkillModel, EmployeeModel
from department_app.database import db


class CRUDEmployee:
    """Employee CRUD class"""
    @staticmethod
    def get(employee_id):
        """Get employee func"""
        employee = department = permission = address = location = skill = None

        emp = EmployeeModel.query.filter_by(id=employee_id).all()
        employee_query = db.session.query(
            EmployeeModel, DepartmentModel, PermissionModel, AddressModel, LocationModel, SkillModel)\
            .join(DepartmentModel).join(PermissionModel).join(AddressModel).join(LocationModel).join(SkillModel)\
            .filter(EmployeeModel.id == employee_id)
        if not emp:
            return None
        for employee, department, permission, address, location, skill in employee_query:
            user_info = {'name': employee.name, 'surname': employee.surname,
                         'date_of_birth': employee.date_of_birth,
                         'salary': employee.salary, 'email': employee.email, 'phone': employee.phone,
                         'date_of_joining': employee.date_of_joining, 'department': department.name,
                         'location': location.name, 'work_address': address.name, 'key_skill': skill.name,
                         'permission': permission.name, 'department_id': employee.department,
                         'employee_id': employee.id, 'location_id': employee.location,
                         'address_id': employee.work_address, 'skill_id': employee.key_skill,
                         'permission_id': employee.permission}
            return user_info
        return False

    @staticmethod
    def update(employee_id, name, surname, date_of_birth, salary, email, phone,
               date_of_joining, department, location, work_address, key_skill,
               permission):
        """Update employee func"""
        logging.info("Update employee method called with parameters: id=%s, name=%s.", employee_id, name)

        try:
            result = EmployeeModel.query.where(EmployeeModel.id == employee_id). \
                update({EmployeeModel.name: name,
                        EmployeeModel.surname: surname,
                        EmployeeModel.date_of_birth: date_of_birth,
                        EmployeeModel.salary: salary,
                        EmployeeModel.email: email,
                        EmployeeModel.phone: phone,
                        EmployeeModel.date_of_joining: date_of_joining,
                        EmployeeModel.department: department,
                        EmployeeModel.location: location,
                        EmployeeModel.work_address: work_address,
                        EmployeeModel.key_skill: key_skill,
                        EmployeeModel.permission: permission})
            db.session.commit()
        except IntegrityError as exception:
            logging.info("The employee contain fields already in use.")
            raise exception
        return bool(result)

    @staticmethod
    def create(name, surname, date_of_birth, salary, email, phone, date_of_joining, department,
               location, work_address, key_skill, permission):
        """Create employee func"""
        employee = EmployeeModel(name=name, surname=surname, date_of_birth=date_of_birth, salary=salary,
                                 email=email, phone=phone, date_of_joining=date_of_joining, department=department,
                                 location=location, work_address=work_address, key_skill=key_skill,
                                 permission=permission)

        try:
            db.session.add(employee)
            db.session.commit()
        except IntegrityError as exception:
            logging.info("The employee contain fields already in use.")
            raise exception

        return employee

    @staticmethod
    def delete(employee_id):
        """Delete employee func"""
        employee = EmployeeModel.query.filter_by(id=employee_id).first()
        if not employee:
            return False
        db.session.delete(employee)
        db.session.commit()
        return True

    @staticmethod
    def get_employee_api(employee_id):
        """Get employee func"""
        employee = EmployeeModel.query.filter_by(id=employee_id).first()
        if not employee:
            return None
        return employee

    @staticmethod
    def get_employee_list():
        """Get employee func"""
        query_join = db.session.query(
            EmployeeModel, DepartmentModel, PermissionModel, AddressModel, LocationModel, SkillModel)\
            .join(DepartmentModel).join(PermissionModel).join(AddressModel).join(LocationModel).join(SkillModel)
        employee_list = []
        employees = query_join.all()
        for employee, department, permission, address, location, skill in employees:
            user_info = {'name': employee.name, 'surname': employee.surname,
                         'date_of_birth': employee.date_of_birth,
                         'salary': employee.salary, 'email': employee.email, 'phone': employee.phone,
                         'date_of_joining': employee.date_of_joining, 'department': department.name,
                         'location': location.name, 'work_address': address.name, 'key_skill': skill.name,
                         'permission': permission.name, 'department_id': employee.department,
                         'employee_id': employee.id, 'location_id': employee.location,
                         'address_id': employee.work_address, 'skill_id': employee.key_skill,
                         'permission_id': employee.permission}
            employee_list.append(user_info)
        return tuple(employee_list)
