"""Manage department page"""
from department_app.service import CRUDDepartment
from department_app.views.base import BaseView


class ManageDepartment(BaseView):
    """Manage department page view"""
    def get_template_name(self):
        return 'manage_departments.html'

    def dispatch_request(self):
        context = {'departments_data': CRUDDepartment.get_department_list()}
        return self.render_template(context)
