"""Employee CRUD"""
from sqlalchemy.exc import IntegrityError
from flask import request
from flask_restful import abort
from department_app.models import DepartmentModel, PermissionModel, AddressModel, LocationModel,\
    SkillModel, EmployeeModel
from department_app.database import db


class CRUDEmployee:
    """Employee CRUD class"""
    @staticmethod
    def create_employee(form=None):
        """Create employee func"""
        if form:
            employee = EmployeeModel(name=form.name.data, surname=form.surname.data,
                                     date_of_birth=form['date_of_birth'].data, salary=form.salary.data,
                                     email=form.email.data, phone=form.phone.data,
                                     date_of_joining=form['date_of_joining'].data,
                                     department=request.form['department'], location=request.form['location'],
                                     work_address=request.form['work_address'], key_skill=request.form['key_skill'],
                                     permission=request.form['permission'])
        else:
            employee = EmployeeModel(name=request.json['name'], surname=request.json['surname'],
                                     date_of_birth=request.json['date_of_birth'], salary=request.json['salary'],
                                     email=request.json['email'], phone=request.json['phone'],
                                     date_of_joining=request.json['date_of_joining'],
                                     department=request.json['department'], location=request.json['location'],
                                     work_address=request.json['work_address'], key_skill=request.json['key_skill'],
                                     permission=request.json['permission'])

        try:
            db.session.add(employee)
            db.session.commit()
        except IntegrityError as exception:
            abort(404, message=f"Exception: {exception}")

    @staticmethod
    def update_employee(employee_id, json):
        """Update employee func"""
        employee = EmployeeModel.query.filter_by(id=employee_id).first()

        employee.name = json['name']
        employee.surname = json['surname']
        employee.date_of_birth = json['date_of_birth']
        employee.salary = json['salary']
        employee.email = json['email']
        employee.phone = json['phone']
        employee.date_of_joining = json['date_of_joining']
        employee.department = json['department']
        employee.location = json['location']
        employee.work_address = json['work_address']
        employee.key_skill = json['key_skill']
        employee.permission = json['permission']
        try:
            db.session.commit()
        except IntegrityError as exception:
            abort(404, message=f"Exception: {exception}")

    @staticmethod
    def delete_employee(employee_id):
        """Delete employee func"""
        if not str(employee_id).isdigit():
            abort(404, message="ID must be a number.")
        employee = EmployeeModel.query.filter_by(id=employee_id).first()
        if not employee:
            abort(404, message=f"Could not find employee with ID: {employee_id}.")
        db.session.delete(employee)
        db.session.commit()

    @staticmethod
    def get_employee(employee_id):
        """Get employee func"""
        employee = department = permission = address = location = skill = None
        if not str(employee_id).isdigit():
            abort(404, message="ID must be a number.")
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
        if not str(employee_id).isdigit():
            abort(404, message="ID must be a number.")
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
