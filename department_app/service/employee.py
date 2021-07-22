"""Employee CRUD"""
from pydantic import ValidationError
from flask import request
from flask_restful import abort
from department_app.models.app_models import db
from department_app.models.app_models import Employee
from department_app.models.employee_schema import EmployeeModel


class CRUDEmployee:
    """Employee CRUD class"""
    @staticmethod
    def create_employee():
        """Create employee func"""
        form_data = request.form
        employee = Employee(name=form_data['name'], surname=form_data['surname'],
                            date_of_birth=form_data['date_of_birth'], salary=form_data['salary'],
                            email=form_data['email'], phone=form_data['phone'],
                            date_of_joining=form_data['date_of_joining'], department=form_data['department'],
                            location=form_data['location'], work_address=form_data['work_address'],
                            key_skill=form_data['key_skill'], permission=form_data['permission'])
        db.session.add(employee)
        db.session.commit()

    @staticmethod
    def update_employee(employee_id):
        """Update employee func"""
        employee = Employee.query.filter_by(id=employee_id).first()
        form_data = request.form

        employee_data = {'name': form_data['name'], 'surname': form_data['surname'],
                         'date_of_birth': form_data['date_of_birth'], 'salary': form_data['salary'],
                         'email': form_data['email'], 'phone': form_data['phone'],
                         'date_of_joining': form_data['date_of_joining'], 'department': form_data['department'],
                         'location': form_data['location'], 'work_address': form_data['work_address'],
                         'key_skill': form_data['key_skill'], 'permission': form_data['permission']}

        try:
            EmployeeModel(**employee_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        employee.name = form_data['name']
        employee.surname = form_data['surname']
        employee.date_of_birth = form_data['date_of_birth']
        employee.salary = form_data['salary']
        employee.email = form_data['email']
        employee.phone = form_data['phone']
        employee.date_of_joining = form_data['date_of_joining']
        employee.department = form_data['department']
        employee.location = form_data['location']
        employee.work_address = form_data['work_address']
        employee.key_skill = form_data['key_skill']
        employee.permission = form_data['permission']
        db.session.commit()

    @staticmethod
    def delete_employee(employee_id):
        """Delete employee func"""
        employee = Employee.query.filter_by(id=employee_id).first()
        db.session.delete(employee)
        db.session.commit()

    @staticmethod
    def get_employee(employee_id):
        """Get employee func"""
        employee = Employee.query.filter_by(id=employee_id).first()
        return employee

    @staticmethod
    def search_employee(emp_primary_skill):
        """Search employee func"""
        employees = Employee.query.filter_by(primary_skill=emp_primary_skill)
        return employees
