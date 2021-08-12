"""Employee CRUD"""
from sqlalchemy.exc import IntegrityError
from pydantic import ValidationError
from flask import request
from flask_restful import abort

from department_app.models import DepartmentModel, PermissionModel, AddressModel, LocationModel,\
    SkillModel, EmployeeModel
from department_app.schemas import EmployeeSchema
from department_app.database import db
from .service import check_id_format


class CRUDEmployee:
    """Employee CRUD class"""
    @staticmethod
    def create_employee(form=None):
        """Create employee func"""
        if form:
            employee_data = {'name': form.name.data, 'surname': form.surname.data,
                             'date_of_birth': form['date_of_birth'].data, 'salary': form.salary.data,
                             'email': form.email.data, 'phone': form.phone.data,
                             'date_of_joining': form['date_of_joining'].data,
                             'department': request.form['department'], 'location': request.form['location'],
                             'work_address': request.form['work_address'], 'key_skill': request.form['key_skill'],
                             'permission': request.form['permission']}
            employee = EmployeeModel(**employee_data)
        else:
            employee_data = {'name': request.json['name'], 'surname': request.json['surname'],
                             'date_of_birth': request.json['date_of_birth'], 'salary': request.json['salary'],
                             'email': request.json['email'], 'phone': request.json['phone'],
                             'date_of_joining': request.json['date_of_joining'],
                             'department': request.json['department'],
                             'location': request.json['location'], 'work_address': request.json['work_address'],
                             'key_skill': request.json['key_skill'], 'permission': request.json['permission']}

            employee = EmployeeModel(**employee_data)

        try:
            EmployeeSchema(**employee_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        try:
            db.session.add(employee)
            db.session.commit()
        except IntegrityError as exception:
            abort(404, message=f"Exception: {exception}")

        return employee

    @staticmethod
    def update_employee(employee_id):
        """Update employee func"""
        employee = CRUDEmployee.get_employee_api(employee_id)

        employee_data = {'name': employee.name, 'surname': employee.surname,
                         'date_of_birth': str(employee.date_of_birth), 'salary': employee.salary,
                         'email': employee.email, 'phone': employee.phone,
                         'date_of_joining': str(employee.date_of_joining), 'department': employee.department,
                         'location': employee.location, 'work_address': employee.work_address,
                         'key_skill': employee.key_skill, 'permission': employee.permission}

        employee_json = request.json
        employee_data.update(employee_json)

        try:
            EmployeeSchema(**employee_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        employee.name = employee_data['name']
        employee.surname = employee_data['surname']
        employee.date_of_birth = employee_data['date_of_birth']
        employee.salary = employee_data['salary']
        employee.email = employee_data['email']
        employee.phone = employee_data['phone']
        employee.date_of_joining = employee_data['date_of_joining']
        employee.department = employee_data['department']
        employee.location = employee_data['location']
        employee.work_address = employee_data['work_address']
        employee.key_skill = employee_data['key_skill']
        employee.permission = employee_data['permission']

        try:
            db.session.commit()
        except IntegrityError as exception:
            abort(404, message=f"Exception: {exception}")

        return employee

    @staticmethod
    def delete_employee(employee_id):
        """Delete employee func"""
        check_id_format(employee_id)

        employee = EmployeeModel.query.filter_by(id=employee_id).first()
        if not employee:
            abort(404, message=f"Could not find employee with ID: {employee_id}.")
        db.session.delete(employee)
        db.session.commit()

    @staticmethod
    def get_employee(employee_id):
        """Get employee func"""
        employee = department = permission = address = location = skill = None
        check_id_format(employee_id)

        emp = EmployeeModel.query.filter_by(id=employee_id).all()
        employee_query = db.session.query(
            EmployeeModel, DepartmentModel, PermissionModel, AddressModel, LocationModel, SkillModel)\
            .join(DepartmentModel).join(PermissionModel).join(AddressModel).join(LocationModel).join(SkillModel)\
            .filter(EmployeeModel.id == employee_id)
        if not emp:
            abort(404, message=f"Could not find employee with ID: {employee_id}.")
        else:
            for employee, department, permission, address, location, skill in employee_query:
                pass
            user_info = {'name': employee.name, 'surname': employee.surname, 'date_of_birth': employee.date_of_birth,
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
    def get_employee_api(employee_id):
        """Get employee func"""
        check_id_format(employee_id)

        employee = EmployeeModel.query.filter_by(id=employee_id).first()
        if not employee:
            abort(404, message=f"Could not find employee with ID: {employee_id}.")
        return employee

    @staticmethod
    def get_all_employee():
        """Get employee func"""
        query_join = db.session.query(
            EmployeeModel, DepartmentModel, PermissionModel, AddressModel, LocationModel, SkillModel)\
            .join(DepartmentModel).join(PermissionModel).join(AddressModel).join(LocationModel).join(SkillModel)
        employee_list = []
        employees = query_join.all()
        for employee, department, permission, address, location_inf, skill_inf in employees:
            user_info = {'name': employee.name, 'surname': employee.surname, 'date_of_birth': employee.date_of_birth,
                         'salary': employee.salary, 'email': employee.email, 'phone': employee.phone,
                         'date_of_joining': employee.date_of_joining, 'department': department.name,
                         'location': location_inf.name, 'work_address': address.name, 'key_skill': skill_inf.name,
                         'permission': permission.name, 'department_id': employee.department,
                         'emp_id': employee.id}
            employee_list.append(user_info)

        return tuple(employee_list)
