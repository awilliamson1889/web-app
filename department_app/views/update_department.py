# pylint: disable=arguments-differ
"""Update department page"""
from sqlalchemy.exc import IntegrityError
from flask import request, redirect, url_for

from department_app.service import CRUDDepartment
from department_app.views.base import BaseView
from department_app.views.forms.forms import DepartmentForm


class UpdateDepartment(BaseView):
    """Update department page view"""
    methods = ['GET', 'POST']

    def get_template_name(self):
        return 'update_department.html'

    def dispatch_request(self, department_id):
        form = DepartmentForm(request.form)
        if request.method == 'POST' and form.validate():
            try:
                CRUDDepartment.update(department_id, form.name.data, form.date_of_creation.data, form.manager.data)
            except IntegrityError:
                context = {'form': form,
                           'message': "Sorry but this department already exist."}
                return self.render_template(context)
            return redirect(url_for('manage_department_page'))

        context = {'form': form,
                   'department_data': CRUDDepartment.get(department_id)}
        return self.render_template(context)
