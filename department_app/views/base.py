"""Base views module"""
from flask.views import View
from flask import render_template


class BaseView(View):
    """Base class for view"""
    def get_template_name(self):
        """
        set template name for rendering
        example:
        def get_template_name():
            return 'my_template.html'
        """
        raise NotImplementedError

    def render_template(self, context):
        """
        render template with some context
        """
        return render_template(self.get_template_name(), **context)
