"""Add skill page"""
from sqlalchemy.exc import IntegrityError
from flask import request, redirect, url_for

from department_app.service import CRUDSkill
from department_app.views.forms.forms import SkillForm
from department_app.views.base import BaseView


class AddSkill(BaseView):
    """Add skill page view"""
    methods = ['GET', 'POST']

    def get_template_name(self):
        return 'add_skill.html'

    def dispatch_request(self):
        form = SkillForm(request.form)
        if request.method == 'POST' and form.validate():
            try:
                CRUDSkill.create(form.name.data)
            except IntegrityError:
                context = {'form': form,
                           'message': 'Sorry but this skill already exist.'}
                return self.render_template(context)
            return redirect(url_for('add_employee'))

        context = {'form': form}
        return self.render_template(context)
