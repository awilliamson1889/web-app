"""Update department page"""
from sqlalchemy.exc import IntegrityError
from flask import request, redirect, url_for

from department_app.service import CRUDDepartment
from department_app.views.base import BaseView
from department_app.views.forms.forms import DepartmentForm


class MainPage(BaseView):
    """Update department page view"""
    methods = ['GET', 'POST']

    def get_template_name(self):
        return 'manage_employee.html'

    def dispatch_request(self):
        return redirect(url_for('manage_employee_page'))
