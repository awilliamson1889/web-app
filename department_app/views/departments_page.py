"""Departments page"""
from flask import request

from department_app.service import CRUDDepartment
from department_app.views.base import BaseView


class DepartmentsPage(BaseView):
    """Departments page view"""
    methods = ['GET', 'POST']

    def get_template_name(self):
        return 'departments.html'

    def dispatch_request(self):
        if request.method == 'POST':
            filters = {'department_name': request.form.get('department_name') or ''}
            context = {'departments_data': CRUDDepartment.get_department_list(filters=filters)}
            return self.render_template(context)

        context = {'departments_data': CRUDDepartment.get_department_list()}
        return self.render_template(context)
