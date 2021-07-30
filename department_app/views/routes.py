"""Routes web-app"""
import logging
from werkzeug.local import LocalProxy
from flask import Blueprint, request, render_template, redirect, url_for, current_app
from department_app.service.employee import CRUDEmployee
from department_app.service.department import CRUDDepartment
from department_app.service.address import CRUDAddress
from department_app.service.location import CRUDLocation
from department_app.service.skill import CRUDSkill
from department_app.service.permission import CRUDPermission
from department_app.views.forms.app_form import AddDepartmentForm, AddSkillForm, AddAddressForm, AddLocationForm, \
    AddPermissionForm


file_log = logging.FileHandler('department_app.log')
console_out = logging.StreamHandler()
logger = LocalProxy(lambda: current_app.logger)
logging.basicConfig(handlers=(file_log, console_out),
                    format='[%(asctime)s | %(levelname)s]: %(message)s',
                    datefmt='%m.%d.%Y %H:%M:%S',
                    level=logging.INFO)

frontend = Blueprint('frontend', __name__)


@frontend.route('/employee/<string:employee_id>')
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


@frontend.route('/departments')
def all_department_page():
    """Return / page"""
    departments = CRUDDepartment.get_all_department()
    logger.info(f'Page successful loaded!')
    return render_template('departments.html', departments_data=departments)


@frontend.route('/employee/search')
def search_employee_page():
    """Return / page"""
    employees = CRUDEmployee.get_all_employee()
    logger.info(f'Page successful loaded!')
    return render_template('people_search.html', employees_data=employees)


@frontend.route('/manage/employee', methods=['POST', 'GET'])
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
def manage_department_page():
    """Return / page"""
    departments = CRUDDepartment.get_all_department()
    logger.info(f'Page successful loaded!')
    return render_template('manage_departments.html', departments_data=departments)


@frontend.route('/add/employee', methods=['POST', 'GET'])
def add_employee_page():
    """Return / page"""
    departments = CRUDDepartment.get_all_department()
    addresses = CRUDAddress.get_all_address()
    locations = CRUDLocation.get_all_location()
    skills = CRUDSkill.get_all_skill()
    permissions = CRUDPermission.get_all_permission()
    logger.info(f'Page successful loaded!')
    return render_template('add_employee.html', departments_data=departments, addresses_data=addresses,
                           locations_data=locations, skills_data=skills, permissions_data=permissions)


@frontend.route('/add/department', methods=['POST', 'GET'])
def add_department_page():
    """Return / page"""
    form = AddDepartmentForm(request.form)
    if request.method == 'POST' and form.validate():
        CRUDDepartment.create_department(form)
        return redirect(url_for('frontend.manage_department_page'))
    logger.info(f'Page successful loaded!')
    return render_template('add_department.html', form=form)


@frontend.route('/create/new/employee', methods=['POST', 'GET'])
def create_new_employee():
    """Return / page"""
    if request.method == 'GET':
        return "The URL /create/new/employee is accessed directly. Try going to '/add/employee' to submit form"
    if request.method == 'POST':
        CRUDEmployee.create_employee()
        logger.info(f'New employee created!')
        return redirect(url_for('frontend.manage_employee_page'))


@frontend.route('/update/employee/data/<string:employee_id>', methods=['POST', 'GET'])
def update_employee(employee_id):
    """Return / page"""
    if request.method == 'GET':
        return "The URL /update/employee/data/<employee_id> is accessed directly. Try going to " \
               "'/update/department/<employee_id>' to submit form"
    if request.method == 'POST':
        CRUDEmployee.update_employee(employee_id)
        logger.info(f'Employee successful updated')
        return redirect(url_for('frontend.manage_employee_page'))


@frontend.route('/update/department/data/<string:department_id>', methods=['POST', 'GET'])
def update_department(department_id):
    """Return / page"""
    if request.method == 'GET':
        return "The URL /update/department/data/<department_id> is accessed directly. Try going to " \
               "'/update/department/<department_id>' to submit form"
    if request.method == 'POST':
        CRUDDepartment.update_department(department_id)
        logger.info(f'Department successful updated!')
        return redirect(url_for('frontend.manage_department_page'))


@frontend.route('/update/department/<string:department_id>', methods=['POST', 'GET'])
def update_department_page(department_id):
    """Return / page"""
    department = CRUDDepartment.get_department(department_id)
    logger.info(f'Page successful loaded!')
    return render_template('update_department.html', department_data=department)


@frontend.route('/update/employee/<string:employee_id>', methods=['POST', 'GET'])
def update_employee_page(employee_id):
    """Return / page"""
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
    logger.info(f'Page successful loaded!')
    return render_template('update_employee.html', employee_data=employee, departments_data=departments,
                           addresses_data=addresses, locations_data=locations, skills_data=skills,
                           permissions_data=permissions)


@frontend.route('/add/skill', methods=['POST', 'GET'])
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
def confirm_delete_employee(employee_id):
    """Return / page"""
    emp_id = employee_id
    logger.info(f'Page successful loaded!')
    return render_template('delete_employee.html', emp_id=emp_id)
