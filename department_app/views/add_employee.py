# pylint: disable=duplicate-code
"""Add employee page"""
from sqlalchemy.exc import IntegrityError
from flask import request, redirect, url_for

from department_app.service import CRUDEmployee, CRUDLocation, CRUDPermission, CRUDDepartment, CRUDAddress, CRUDSkill
from department_app.views.forms.forms import EmployeeForm
from department_app.views.base import BaseView


class AddEmployee(BaseView):
    """Add employee page view"""
    methods = ['GET', 'POST']

    def get_template_name(self):
        return 'add_employee.html'

    def dispatch_request(self):
        form = EmployeeForm(request.form)
        form.work_address.choices = [(address['id'], address['name']) for address in CRUDAddress.get_address_list()]
        form.department.choices = [(dep.department_id, dep.name) for dep in CRUDDepartment.get_department_list()]
        form.location.choices = [(loc['id'], loc['name']) for loc in CRUDLocation.get_location_list()]
        form.key_skill.choices = [(skill['id'], skill['name']) for skill in CRUDSkill.get_skill_list()]
        form.permission.choices = [(perm['id'], perm['name']) for perm in CRUDPermission.get_permission_list()]

        if request.method == 'POST' and form.validate():
            try:
                CRUDEmployee.create(form.name.data, form.surname.data, form.date_of_birth.data,
                                    form.salary.data, form.email.data, form.phone.data, form.date_of_joining.data,
                                    form.department.data, form.location.data, form.work_address.data,
                                    form.key_skill.data,
                                    form.permission.data)
            except IntegrityError:
                context = {'form': form,
                           'message': 'Sorry but this employee have same fields with another employee.'}
                return self.render_template(context)
            return redirect(url_for('manage_employee_page'))

        context = {'form': form}
        return self.render_template(context)
