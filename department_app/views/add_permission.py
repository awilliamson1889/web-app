"""Add permission page"""
from sqlalchemy.exc import IntegrityError
from flask import request, redirect, url_for

from department_app.service import CRUDPermission
from department_app.views.forms.forms import PermissionForm
from department_app.views.base import BaseView


class AddPermission(BaseView):
    """Add permission page view"""
    methods = ['GET', 'POST']

    def get_template_name(self):
        return 'add_permission.html'

    def dispatch_request(self):
        form = PermissionForm(request.form)
        if request.method == 'POST' and form.validate():
            try:
                CRUDPermission.create(form.name.data)
            except IntegrityError:
                context = {'form': form,
                           'message': 'Sorry but this permission already exist.'}
                return self.render_template(context)
            return redirect(url_for('add_employee'))

        context = {'form': form}
        return self.render_template(context)
