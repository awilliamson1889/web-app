"""Routes web-app"""
import logging
from werkzeug.security import check_password_hash
from werkzeug.local import LocalProxy
from department_app.models.app_models import Employee
from flask_login import login_user, logout_user, login_required
from flask import Blueprint, request, render_template, redirect, url_for, current_app, flash
from department_app.service.employee import CRUDEmployee
from department_app.service.department import CRUDDepartment
from department_app.service.address import CRUDAddress
from department_app.service.location import CRUDLocation
from department_app.service.skill import CRUDSkill
from department_app.service.permission import CRUDPermission
from department_app.views.forms.app_form import AddDepartmentForm, AddSkillForm, AddAddressForm, AddLocationForm, \
    AddPermissionForm, AddEmployeeForm


file_log = logging.FileHandler('department_app.log')
console_out = logging.StreamHandler()
logger = LocalProxy(lambda: current_app.logger)
logging.basicConfig(handlers=(file_log, console_out),
                    format='[%(asctime)s | %(levelname)s]: %(message)s',
                    datefmt='%m.%d.%Y %H:%M:%S',
                    level=logging.INFO)

frontend = Blueprint('frontend', __name__)


@frontend.route('/employee/<string:employee_id>')
@login_required
def user_page(employee_id):
    """Return / page"""
    if not str(employee_id).isdigit():
        logger.info(f'Wrong ID format, employee_id={employee_id}')
        return "ID must be a number.", 404
    employee = CRUDEmployee.get_employee(employee_id)
    if not employee:
        logger.info(f'Could not find employee with ID: {employee_id}.')
        return f"Could not find employee with ID: {employee_id}.", 404
    logger.info(f'Page successful loaded!')
    return render_template('profile.html', employee_data=employee)


@frontend.route('/department/<string:department_id>')
@login_required
def department_page(department_id):
    """Return / page"""
    if not str(department_id).isdigit():
        logger.info(f'Wrong ID format, department_id={department_id}')
        return "ID must be a number.", 404
    department = CRUDDepartment.get_department(department_id)
    if not department:
        logger.info(f'Could not find department with ID: {department_id}.')
        return f"Could not find department with ID: {department_id}.", 404
    employees = CRUDEmployee.get_all_employee(department_id)
    logger.info(f'Page successful loaded!')
    return render_template('department.html', department_data=department, employees_data=employees)


@frontend.route('/departments', methods=['POST', 'GET'])
@login_required
def all_department_page():
    """Return / page"""
    form = request.form
    if request.method == 'POST':
        departments = CRUDDepartment.get_all_department(form['search'])
        logger.info(f'Page successful loaded!')
        return render_template('departments.html', departments_data=departments)
    departments = CRUDDepartment.get_all_department()
    logger.info(f'Page successful loaded!')
    return render_template('departments.html', departments_data=departments)


@frontend.route('/employee/search', methods=['POST', 'GET'])
@login_required
def search_employee_page():
    """Return / page"""
    form = request.form
    locations = CRUDLocation.get_all_location()
    skills = CRUDSkill.get_all_skill()
    if request.method == 'POST':
        employees = CRUDEmployee.get_all_employee(skill=form['key_skill'], location=form['location'],
                                                  name=form['search'])
        logger.info(f'Page successful loaded!')
        return render_template('people_search.html', employees_data=employees, locations_data=locations,
                               skills_data=skills)
    employees = CRUDEmployee.get_all_employee()
    logger.info(f'Page successful loaded!')
    return render_template('people_search.html', employees_data=employees, locations_data=locations,
                           skills_data=skills)


@frontend.route('/manage/employee', methods=['POST', 'GET'])
@login_required
def manage_employee_page():
    """Return / page"""
    if request.method == 'GET':
        employees = CRUDEmployee.get_all_employee()
        departments = CRUDDepartment.get_all_department()
        logger.info(f'Page successful loaded with GET method!')
        return render_template('manage_employees.html', employees_data=employees, departments_data=departments)
    if request.method == 'POST':
        form_data = request.form
        employees = CRUDEmployee.get_all_employee(department_id=form_data['department'], date1=form_data['date1'],
                                                  date2=form_data['date2'])
        departments = CRUDDepartment.get_all_department()
        logger.info(f'Page successful loaded with POST method!')
        return render_template('manage_employees.html', employees_data=employees, departments_data=departments)


@frontend.route('/manage/department')
@login_required
def manage_department_page():
    """Return / page"""
    departments = CRUDDepartment.get_all_department()
    logger.info(f'Page successful loaded!')
    return render_template('manage_departments.html', departments_data=departments)


@frontend.route('/add/employee', methods=['POST', 'GET'])
@login_required
def add_employee_page():
    """Return / page"""
    form = AddEmployeeForm(request.form)
    form.work_address.choices = [(address['address_id'], address['name']) for address in CRUDAddress.get_all_address()]
    form.department.choices = [(dep['dep_id'], dep['name']) for dep in CRUDDepartment.get_all_department()]
    form.location.choices = [(loc['location_id'], loc['name']) for loc in CRUDLocation.get_all_location()]
    form.key_skill.choices = [(skill['skill_id'], skill['name']) for skill in CRUDSkill.get_all_skill()]
    form.permission.choices = [(perm['permission_id'], perm['name']) for perm in CRUDPermission.get_all_permission()]
    if request.method == 'POST' and form.validate():
        CRUDEmployee.create_employee(form)
        logger.info(f'New employee created!')
        return redirect(url_for('frontend.manage_employee_page'))
    logger.info(f'Page successful loaded!')
    return render_template('add_employee.html', form=form)


@frontend.route('/add/department', methods=['POST', 'GET'])
@login_required
def add_department_page():
    """Return / page"""
    form = AddDepartmentForm(request.form)
    if request.method == 'POST' and form.validate():
        CRUDDepartment.create_department(form)
        return redirect(url_for('frontend.manage_department_page'))
    logger.info(f'Page successful loaded!')
    return render_template('add_department.html', form=form)


@frontend.route('/update/department/<string:department_id>', methods=['POST', 'GET'])
@login_required
def update_department_page(department_id):
    form = AddDepartmentForm(request.form)
    if request.method == 'POST' and form.validate():
        CRUDDepartment.update_department(department_id)
        logger.info(f'Department successful updated!')
        return redirect(url_for('frontend.manage_department_page'))
    """Return / page"""
    department = CRUDDepartment.get_department(department_id)
    logger.info(f'Page successful loaded!')
    return render_template('update_department.html', department_data=department, form=form)


@frontend.route('/update/employee/<string:employee_id>', methods=['POST', 'GET'])
@login_required
def update_employee_page(employee_id):
    """Return / page"""
    form = AddEmployeeForm(request.form)
    form.emp_id = employee_id
    form.work_address.choices = [(address['address_id'], address['name']) for address in CRUDAddress.get_all_address()]
    form.department.choices = [(dep['dep_id'], dep['name']) for dep in CRUDDepartment.get_all_department()]
    form.location.choices = [(loc['location_id'], loc['name']) for loc in CRUDLocation.get_all_location()]
    form.key_skill.choices = [(skill['skill_id'], skill['name']) for skill in CRUDSkill.get_all_skill()]
    form.permission.choices = [(perm['permission_id'], perm['name']) for perm in CRUDPermission.get_all_permission()]

    departments = CRUDDepartment.get_all_department()
    addresses = CRUDAddress.get_all_address()
    locations = CRUDLocation.get_all_location()
    skills = CRUDSkill.get_all_skill()
    permissions = CRUDPermission.get_all_permission()

    if not str(employee_id).isdigit():
        return "ID must be a number.", 404
    employee = CRUDEmployee.get_employee(employee_id)
    if not employee:
        return f"Could not find employee with ID: {employee_id}.", 404
    if request.method == 'POST' and form.validate():
        CRUDEmployee.update_employee(employee_id)
        logger.info(f'Employee successful updated')
        return redirect(url_for('frontend.manage_employee_page'))
    logger.info(f'Page successful loaded!')
    return render_template('update_employee.html', employee_data=employee, departments_data=departments,
                           addresses_data=addresses, locations_data=locations, skills_data=skills,
                           permissions_data=permissions, form=form)


@frontend.route('/add/skill', methods=['POST', 'GET'])
@login_required
def add_skill_page():
    """Return / page"""
    form = AddSkillForm(request.form)
    if request.method == 'POST' and form.validate():
        CRUDSkill.create_skill(form)
        logger.info(f'Page successful loaded!')
        return redirect(url_for('frontend.add_employee_page'))
    logger.info(f'Page successful loaded!')
    return render_template('add_skill.html', form=form)


@frontend.route('/add/address', methods=['POST', 'GET'])
@login_required
def add_address_page():
    """Return / page"""
    form = AddAddressForm(request.form)
    if request.method == 'POST' and form.validate():
        CRUDAddress.create_address(form)
        logger.info(f'Page successful loaded!')
        return redirect(url_for('frontend.add_employee_page'))
    logger.info(f'Page successful loaded!')
    return render_template('add_address.html', form=form)


@frontend.route('/add/location', methods=['POST', 'GET'])
@login_required
def add_location_page():
    """Return / page"""
    form = AddLocationForm(request.form)
    if request.method == 'POST' and form.validate():
        CRUDLocation.create_location(form)
        logger.info(f'Page successful loaded!')
        return redirect(url_for('frontend.add_employee_page'))
    logger.info(f'Page successful loaded!')
    return render_template('add_location.html', form=form)


@frontend.route('/add/permission', methods=['POST', 'GET'])
@login_required
def add_permission_page():
    """Return / page"""
    form = AddPermissionForm(request.form)
    if request.method == 'POST' and form.validate():
        CRUDPermission.create_permission(form)
        logger.info(f'Page successful loaded!')
        return redirect(url_for('frontend.add_employee_page'))
    logger.info(f'Page successful loaded!')
    return render_template('add_permission.html', form=form)


@frontend.route('/delete-employee/<string:employee_id>')
@login_required
def confirm_delete_employee(employee_id):
    """Return / page"""
    emp_id = employee_id
    logger.info(f'Page successful loaded!')
    return render_template('delete_employee.html', emp_id=emp_id)


@frontend.route('/delete/employee/<string:employee_id>', methods=['POST', 'GET'])
@login_required
def delete_employee(employee_id):
    """Return / page"""
    CRUDEmployee.delete_employee(int(employee_id))
    return redirect(url_for('frontend.manage_employee_page'))

###############################################################################################################


@frontend.route('/login', methods=['POST', 'GET'])
def login_page():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
        employee = Employee.query.filter_by(email=login).first()

        if employee and check_password_hash(employee.password, password):
            login_user(employee)

            return redirect(url_for('frontend.user_page', employee_id=employee.id))
        else:
            flash('Login or password not correct')
    else:
        flash('Please fill login and password fields')
    return render_template('login.html')


@frontend.route('/register', methods=['POST', 'GET'])
def register():
    pass


@frontend.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect(url_for('frontend.login_page'))


@frontend.after_request
def redirect_to_login(response):
    if response.status_code == 401:
        return redirect(url_for('frontend.login_page'))

    return response
