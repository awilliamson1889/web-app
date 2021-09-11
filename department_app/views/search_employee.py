"""Search employee page"""
from flask import request

from department_app.service import CRUDLocation, CRUDEmployee, CRUDSkill
from department_app.views.base import BaseView
from department_app.models import LocationModel, SkillModel, EmployeeModel


class SearchEmployee(BaseView):
    """Search employee page view"""
    methods = ['GET', 'POST']

    def get_template_name(self):
        return 'people_search.html'

    def dispatch_request(self):
        if request.method == 'POST':
            filters = {LocationModel.id: request.form.get('location') or '',
                       SkillModel.id: request.form.get('key_skill') or '',
                       EmployeeModel.surname: request.form.get('employee_surname') or ''}
            context = {'locations_data': CRUDLocation.get_location_list(),
                       'skills_data': CRUDSkill.get_skill_list(),
                       'employees_data': CRUDEmployee.get_employee_list(filters=filters)}
            return self.render_template(context)

        context = {'locations_data': CRUDLocation.get_location_list(),
                   'skills_data': CRUDSkill.get_skill_list(),
                   'employees_data': CRUDEmployee.get_employee_list()}
        return self.render_template(context)
