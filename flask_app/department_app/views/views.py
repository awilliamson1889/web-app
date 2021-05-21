"""Flask views"""
from flask import render_template
from department_app import app
from flask.views import View


class TestPage(View):
    """Test class"""
    def dispatch_request(self):
        """Test function"""
        return render_template('test_page.html')


app.add_url_rule('/', view_func=TestPage.as_view('test_page'))
