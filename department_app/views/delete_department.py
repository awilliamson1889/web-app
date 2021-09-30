# pylint: disable=arguments-differ
"""Delete employee page"""
from flask import render_template, request, redirect, url_for

from department_app.service import CRUDDepartment
from department_app.views.base import BaseView


class DeleteDepartment(BaseView):
    """Delete employee page view"""
    methods = ['GET', 'POST']

    def get_template_name(self):
        return 'delete_department.html'

    def dispatch_request(self, department_id):
        if request.method == 'POST':
            CRUDDepartment.delete(department_id)
            return redirect(url_for('manage_department_page'))

        return render_template('delete_department.html')
