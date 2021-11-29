"""Add department page"""
from sqlalchemy.exc import IntegrityError
from flask import request, redirect, url_for

from department_app.service import CRUDDepartment
from department_app.views.forms.forms import DepartmentForm
from department_app.views.base import BaseView


class AddDepartment(BaseView):
    """Add department page view"""
    methods = ['GET', 'POST']

    def get_template_name(self):
        return 'add_department.html'

    def dispatch_request(self):
        form = DepartmentForm(request.form)
        if request.method == 'POST' and form.validate():
            try:
                CRUDDepartment.create(form.name.data, form.date_of_creation.data, form.manager.data)
            except IntegrityError:
                context = {'form': form,
                           'message': "Sorry but this department already exist."}
                return self.render_template(context)
            return redirect(url_for('add_employee'))

        context = {'form': form}
        return self.render_template(context)
