"""Add address page"""
from sqlalchemy.exc import IntegrityError
from flask import request, redirect, url_for

from department_app.service import CRUDAddress
from department_app.views.forms.forms import AddressForm
from department_app.views.base import BaseView


class AddAddress(BaseView):
    """Add address page view"""
    methods = ['POST', 'GET']

    def get_template_name(self):
        return 'add_address.html'

    def dispatch_request(self):
        form = AddressForm(request.form)
        if request.method == 'POST' and form.validate():
            try:
                CRUDAddress.create(form.name.data)
            except IntegrityError:
                context = {'form': form,
                           'message': "Sorry but this address already exist."}
                return self.render_template(context)
            return redirect(url_for('add_employee'))

        context = {'form': form}
        return self.render_template(context)
