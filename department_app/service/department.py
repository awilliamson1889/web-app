"""Department CRUD"""
from flask import request
from department_app.models.app_models import db, Department, Employee
from department_app.views.forms.app_form import AddDepartmentForm


class CRUDDepartment:
    """Employee CRUD class"""
    @staticmethod
    def delete_department(department_id):
        """Delete department func"""
        Department.query.filter_by(id=department_id).delete()
        db.session.commit()

    @staticmethod
    def create_department(form):
        """Create department func"""
        employee = Department(name=form.name.data, date_of_creation=form.date_of_creation.data,
                              manager=form.manager.data)
        db.session.add(employee)
        db.session.commit()

    @staticmethod
    def get_all_department():
        """Get department func"""
        department_list = []
        departments = Department.query.all()
        for department in departments:
            employee = Employee.query.filter_by(department=department.id).all()
            department_info = {'name': department.name, 'manager': department.manager,
                               'date_of_creation': department.date_of_creation,
                               'emp_count': len(Employee.query.filter_by(department=department.id).all()),
                               'dep_salary': sum([x.salary for x in employee]),
                               'dep_id': department.id}
            department_list.append(department_info)
        return tuple(department_list)

    @staticmethod
    def get_department(department_id):
        """Get department func"""
        department_query = Department.query.filter_by(id=department_id).all()
        if len(list(department_query)) != 0:
            for department in department_query:
                department_info = {'name': department.name, 'manager': department.manager,
                                   'date_of_creation': department.date_of_creation,
                                   'emp_count': len(Employee.query.filter_by(department=department.id).all()),
                                   'dep_id': department.id}
            return department_info
        return False

    @staticmethod
    def update_department(department_id):
        """Update employee func"""
        department = Department.query.filter_by(id=department_id).first()
        form_data = request.form

        department.name = form_data['name']
        department.manager = form_data['manager']
        department.date_of_creation = form_data['date_of_creation']

        db.session.commit()
