"""Add location page"""
from sqlalchemy.exc import IntegrityError
from flask import request, redirect, url_for

from department_app.service import CRUDLocation
from department_app.views.forms.forms import LocationForm
from department_app.views.base import BaseView


class AddLocation(BaseView):
    """Add location page view"""
    methods = ['GET', 'POST']

    def get_template_name(self):
        return 'add_location.html'

    def dispatch_request(self):
        form = LocationForm(request.form)
        if request.method == 'POST' and form.validate():
            try:
                CRUDLocation.create(form.name.data)
            except IntegrityError:
                context = {'form': form,
                           'message': 'Sorry but this location already exist.'}
                return self.render_template(context)
            return redirect(url_for('add_employee'))

        context = {'form': form}
        return self.render_template(context)
