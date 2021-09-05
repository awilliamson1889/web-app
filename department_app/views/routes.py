"""Routes web-app"""
from sqlalchemy.exc import IntegrityError
from flask_restful import abort
from flask import Blueprint, render_template, request, redirect, url_for

from department_app.service import CRUDDepartment, CRUDAddress, CRUDSkill, CRUDEmployee, CRUDLocation, CRUDPermission
from department_app.views.forms.forms import DepartmentForm, SkillForm, AddressForm, LocationForm, \
    PermissionForm, EmployeeForm
from department_app.models import DepartmentModel, PermissionModel, AddressModel, LocationModel,\
    SkillModel, EmployeeModel

frontend = Blueprint('frontend', __name__)
"""
ADD TEMPLATES
"""


@frontend.route('/')
def test():
    return 'Hello World'


@frontend.route('/add/address', methods=['POST', 'GET'])
def add_address():
    form = AddressForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            CRUDAddress.create(form.name.data)
        except IntegrityError:
            message = "Sorry but this address already exist."
            return render_template('add_address.html', form=form, message=message)
        return redirect(url_for('frontend.add_employee'))
    else:
        return render_template('add_address.html', form=form)


@frontend.route('/add/department', methods=['POST', 'GET'])
def add_department():
    form = DepartmentForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            CRUDDepartment.create(form.name.data, form.date_of_creation.data, form.manager.data)
        except IntegrityError:
            message = "Sorry but this department already exist."
            return render_template('add_department.html', form=form, message=message)
        return redirect(url_for('frontend.add_employee'))
    else:
        return render_template('add_department.html', form=form)


@frontend.route('/add/employee', methods=['POST', 'GET'])
def add_employee():
    form = EmployeeForm(request.form)
    form.work_address.choices = [(address['id'], address['name']) for address in CRUDAddress.get_address_list()]
    form.department.choices = [(dep['department_id'], dep['name']) for dep in CRUDDepartment.get_department_list()]
    form.location.choices = [(loc['id'], loc['name']) for loc in CRUDLocation.get_location_list()]
    form.key_skill.choices = [(skill['id'], skill['name']) for skill in CRUDSkill.get_skill_list()]
    form.permission.choices = [(perm['id'], perm['name']) for perm in CRUDPermission.get_permission_list()]

    if request.method == 'POST' and form.validate():
        try:
            CRUDEmployee.create(form.name.data, form.surname.data, form.date_of_birth.data,
                                form.salary.data, form.email.data, form.phone.data, form.date_of_joining.data,
                                form.department.data, form.location.data, form.work_address.data, form.key_skill.data,
                                form.permission.data)
        except IntegrityError:
            message = "Sorry but this employee have same fields with another employee."
            return render_template('add_employee.html', form=form, message=message)
        return redirect(url_for('frontend.manage_employee_page'))
    else:
        return render_template('add_employee.html', form=form)


@frontend.route('/add/location', methods=['POST', 'GET'])
def add_location():
    form = LocationForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            CRUDLocation.create(form.name.data)
        except IntegrityError:
            message = "Sorry but this location already exist."
            return render_template('add_location.html', form=form, message=message)
        return redirect(url_for('frontend.add_employee'))
    else:
        return render_template('add_location.html', form=form)


@frontend.route('/add/permission', methods=['POST', 'GET'])
def add_permission():
    form = PermissionForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            CRUDPermission.create(form.name.data)
        except IntegrityError:
            message = "Sorry but this permission already exist."
            return render_template('add_permission.html', form=form, message=message)
        return redirect(url_for('frontend.add_employee'))
    else:
        return render_template('add_permission.html', form=form)


@frontend.route('/add/skill', methods=['POST', 'GET'])
def add_skill():
    form = SkillForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            CRUDSkill.create(form.name.data)
        except IntegrityError:
            message = "Sorry but this skill already exist."
            return render_template('add_skill.html', form=form, message=message)
        return redirect(url_for('frontend.add_employee'))
    else:
        return render_template('add_skill.html', form=form)


"""
DELETE TEMPLATES
"""


@frontend.route('/delete-employee/<string:employee_id>', methods=['POST', 'GET'])
def delete_employee(employee_id):
    if request.method == 'POST':
        CRUDEmployee.delete(employee_id)
        return redirect(url_for('frontend.manage_employee_page'))
    else:
        return render_template('delete_employee.html')


"""
PAGES TEMPLATES
"""


@frontend.route('/departments', methods=['POST', 'GET'])
def departments_page():
    if request.method == 'POST':
        filters = {'department_name': request.form.get('department_name') or ''}
        departments = CRUDDepartment.get_department_list(filters=filters)
        return render_template('departments.html', departments_data=departments)
    else:
        departments = CRUDDepartment.get_department_list()
        return render_template('departments.html', departments_data=departments)


@frontend.route('/department/<string:department_id>')
def department_page(department_id):
    department = CRUDDepartment.get(department_id)
    employees = CRUDEmployee.get_employee_list()
    return render_template('department.html', department_data=department, employees_data=employees)


@frontend.route('/employee/<string:employee_id>')
def employee_page(employee_id):
    employee = CRUDEmployee.get(employee_id)
    return render_template('profile.html', employee_data=employee)


@frontend.route('/manage/department')
def manage_department_page():
    departments = CRUDDepartment.get_department_list()
    return render_template('manage_departments.html', departments_data=departments)


@frontend.route('/manage/employee', methods=['GET', 'POST'])
def manage_employee_page():
    departments = CRUDDepartment.get_department_list()

    if request.method == 'POST':
        filters = {DepartmentModel.id: request.form.get('department') or '',
                   'date1': request.form.get('date1') or '',
                   'date2': request.form.get('date2') or '9999-12-12'}

        employees = CRUDEmployee.get_employee_list(filters=filters)
        return render_template('manage_employees.html', employees_data=employees, departments_data=departments)
    else:
        employees = CRUDEmployee.get_employee_list()
        return render_template('manage_employees.html', employees_data=employees, departments_data=departments)


@frontend.route('/search/employee', methods=['GET', 'POST'])
def search_employee_page():
    locations = CRUDLocation.get_location_list()
    skills = CRUDSkill.get_skill_list()

    if request.method == 'POST':
        filters = {LocationModel.id: request.form.get('location') or '',
                   SkillModel.id: request.form.get('key_skill') or '',
                   EmployeeModel.surname: request.form.get('employee_surname') or ''}

        employees = CRUDEmployee.get_employee_list(filters=filters)
        return render_template('people_search.html', employees_data=employees, locations_data=locations,
                               skills_data=skills)
    else:
        employees = CRUDEmployee.get_employee_list()
        return render_template('people_search.html', employees_data=employees, locations_data=locations,
                               skills_data=skills)


"""
UPDATE TEMPLATES
"""


@frontend.route('/update-department/<string:department_id>', methods=['POST', 'GET'])
def update_department(department_id):
    form = DepartmentForm(request.form)
    department = CRUDDepartment.get(department_id)

    if request.method == 'POST' and form.validate():
        try:
            CRUDDepartment.update(department_id, form.name.data, form.date_of_creation.data, form.manager.data)
        except IntegrityError:
            message = "Sorry but this department already exist."
            return render_template('add_department.html', form=form, message=message)
        return redirect(url_for('frontend.manage_department_page'))
    else:
        return render_template('update_department.html', department_data=department, form=form)


@frontend.route('/update-employee/<string:employee_id>', methods=['POST', 'GET'])
def update_employee(employee_id):
    form = EmployeeForm(request.form)
    form.work_address.choices = [(address['id'], address['name']) for address in CRUDAddress.get_address_list()]
    form.department.choices = [(dep['department_id'], dep['name']) for dep in CRUDDepartment.get_department_list()]
    form.location.choices = [(loc['id'], loc['name']) for loc in CRUDLocation.get_location_list()]
    form.key_skill.choices = [(skill['id'], skill['name']) for skill in CRUDSkill.get_skill_list()]
    form.permission.choices = [(perm['id'], perm['name']) for perm in CRUDPermission.get_permission_list()]

    employee = CRUDEmployee.get(employee_id)

    if request.method == 'POST' and form.validate():
        try:
            CRUDEmployee.update(employee_id, form.name.data, form.surname.data, form.date_of_birth.data,
                                form.salary.data, form.email.data, form.phone.data, form.date_of_joining.data,
                                form.department.data, form.location.data, form.work_address.data, form.key_skill.data,
                                form.permission.data)
        except IntegrityError:
            message = "Sorry but this employee have same fields with another employee."
            return render_template('add_employee.html', form=form, message=message)
        return redirect(url_for('frontend.manage_employee_page'))
    else:
        return render_template('update_employee.html', employee_data=employee, form=form)


"""
I DON'T KNOW FOR WHAT BUT ...
"""


@frontend.route('/logout')
def logout():
    return "LOGOUT"


"""
NOT IMPLEMENTED METHODS
UPDATE ADDRESS
UPDATE LOCATION
UPDATE PERMISSION
UPDATE SKILL
LOGIN PAGE
"""