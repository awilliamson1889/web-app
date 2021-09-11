# pylint: disable=arguments-differ
"""Employee page"""
from department_app.service import CRUDEmployee
from department_app.views.base import BaseView


class EmployeePage(BaseView):
    """Employee page view"""
    def get_template_name(self):
        return 'profile.html'

    def dispatch_request(self, employee_id):
        context = {'employee_data': CRUDEmployee.get(employee_id)}
        return self.render_template(context)
