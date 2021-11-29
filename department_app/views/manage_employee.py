"""Manage employee page"""
from flask import request

from department_app.service import CRUDDepartment, CRUDEmployee
from department_app.views.base import BaseView
from department_app.models import DepartmentModel


class ManageEmployee(BaseView):
    """Manage employee page view"""
    methods = ['GET', 'POST']

    def get_template_name(self):
        return 'manage_employees.html'

    def dispatch_request(self):
        if request.method == 'POST':
            filters = {DepartmentModel.id: request.form.get('department') or '',
                       'date1': request.form.get('date1') or '',
                       'date2': request.form.get('date2') or '9999-12-12'}
            context = {'employees_data': CRUDEmployee.get_employee_list(filters=filters),
                       'departments_data': CRUDDepartment.get_department_list()}

            return self.render_template(context)

        context = {'employees_data': CRUDEmployee.get_employee_list(),
                   'departments_data': CRUDDepartment.get_department_list()}
        return self.render_template(context)
