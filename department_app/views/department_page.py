# pylint: disable=arguments-differ
"""Department page"""
from department_app.service import CRUDDepartment, CRUDEmployee
from department_app.views.base import BaseView


class DepartmentPage(BaseView):
    """Department page view"""
    def get_template_name(self):
        return 'department.html'

    def dispatch_request(self, department_id):
        context = {'department_data': CRUDDepartment.get(department_id),
                   'employees_data': CRUDEmployee.get_employee_list()}
        return self.render_template(context)
