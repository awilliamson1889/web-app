# pylint: disable=arguments-differ
"""Delete employee page"""
from flask import render_template, request, redirect, url_for

from department_app.service import CRUDEmployee
from department_app.views.base import BaseView


class DeleteEmployee(BaseView):
    """Delete employee page view"""
    methods = ['GET', 'POST']

    def get_template_name(self):
        return 'delete_employee'

    def dispatch_request(self, employee_id):
        if request.method == 'POST':
            CRUDEmployee.delete(employee_id)
            return redirect(url_for('manage_employee_page'))

        return render_template('delete_employee.html')
