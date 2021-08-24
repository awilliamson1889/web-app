"""Routes web-app"""
from flask import Blueprint, render_template


frontend = Blueprint('frontend', __name__)

"""
ADD TEMPLATES
"""


@frontend.route('/')
def test():
    return 'Hello World'


@frontend.route('/add/address')
def add_address():
    return render_template('add_address.html')


@frontend.route('/add/department')
def add_department():
    return render_template('add_department.html')


@frontend.route('/add/employee')
def add_employee():
    return render_template('add_employee.html')


@frontend.route('/add/location')
def add_location():
    return render_template('add_location.html')


@frontend.route('/add/permission')
def add_permission():
    return render_template('add_permission.html')


@frontend.route('/add/skill')
def add_skill():
    return render_template('add_skill.html')


"""
DELETE TEMPLATES
"""


@frontend.route('/delete/employee')
def delete_employee():
    return render_template('delete_employee.html')


"""
PAGES TEMPLATES
"""


@frontend.route('/departments')
def departments_page():
    return render_template('departments.html')


@frontend.route('/department/<string:department_id>')
def department_page(department_id):
    return render_template('department.html')


@frontend.route('/employee/<string:employee_id>')
def employee_page(employee_id):
    return render_template('profile.html')


@frontend.route('/manage/department')
def manage_department_page():
    return render_template('manage_departments.html')


@frontend.route('/manage/employee')
def manage_employee_page():
    return render_template('manage_employees.html')


@frontend.route('/search/employee')
def search_employee_page():
    return render_template('people_search.html')


"""
UPDATE TEMPLATES
"""


@frontend.route('/update-department/<string:department_id>')
def update_department(department_id):
    return render_template('update_department.html')


@frontend.route('/update-employee/<string:employee_id>')
def update_employee(employee_id):
    return render_template('update_employee.html')


"""
I DON'T KNOW FOR WHAT BUT ...
"""


@frontend.route('/logout')
def logout(employee_id):
    return "LOGOUT"

