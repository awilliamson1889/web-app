"""Employee CRUD"""
from flask import request
from department_app.models.app_models import db, Department, Permission, Address, Location, Skill, Employee


class CRUDEmployee:
    """Employee CRUD class"""
    @staticmethod
    def create_employee():
        """Create employee func"""
        form_data = request.form
        employee = Employee(name=form_data['name'], surname=form_data['surname'],
                            date_of_birth=form_data['date_of_birth'], salary=form_data['salary'],
                            email=form_data['email'], phone=form_data['phone'],
                            date_of_joining=form_data['date_of_joining'], department=form_data['department'],
                            location=form_data['location'], work_address=form_data['work_address'],
                            key_skill=form_data['key_skill'], permission=form_data['permission'])
        db.session.add(employee)
        db.session.commit()

    @staticmethod
    def update_employee(employee_id):
        """Update employee func"""
        employee = Employee.query.filter_by(id=employee_id).first()
        form_data = request.form

        employee.name = form_data['name']
        employee.surname = form_data['surname']
        employee.date_of_birth = form_data['date_of_birth']
        employee.salary = form_data['salary']
        employee.email = form_data['email']
        employee.phone = form_data['phone']
        employee.date_of_joining = form_data['date_of_joining']
        employee.department = form_data['department']
        employee.location = form_data['location']
        employee.work_address = form_data['work_address']
        employee.key_skill = form_data['key_skill']
        employee.permission = form_data['permission']
        db.session.commit()

    @staticmethod
    def delete_employee(employee_id):
        """Delete employee func"""
        employee = Employee.query.filter_by(id=employee_id).first()
        db.session.delete(employee)
        db.session.commit()

    @staticmethod
    def get_employee(employee_id):
        """Get employee func"""
        employee = department = permission = address = location = skill = None
        employee_query = db.session.query(Employee, Department, Permission, Address, Location, Skill).join(Department)\
            .join(Permission).join(Address).join(Location).join(Skill).filter(Employee.id == employee_id)
        if len(list(employee_query)) != 0:
            for employee, department, permission, address, location, skill in employee_query:
                pass
            user_info = {'name': employee.name, 'surname': employee.surname, 'date_of_birth': employee.date_of_birth,
                         'salary': employee.salary, 'email': employee.email, 'phone': employee.phone,
                         'date_of_joining': employee.date_of_joining, 'department': department.name,
                         'location': location.name, 'work_address': address.name, 'key_skill': skill.name,
                         'permission': permission.name, 'department_id': employee.department,
                         'emp_id': employee.id, 'location_id': employee.location, 'address_id': employee.work_address,
                         'skill_id': employee.key_skill, 'permission_id': employee.permission}
            return user_info
        return False

    @staticmethod
    def search_employee(emp_primary_skill):
        """Search employee func"""
        employees = Employee.query.filter_by(primary_skill=emp_primary_skill)
        return employees

    @staticmethod
    def get_all_employee(department_id='No', date1='', date2=''):
        """Get employee func"""
        employee_list = []
        if date1 and date2 != '' and department_id == 'No':
            employees = db.session.query(Employee, Department, Permission, Address, Location, Skill).join(Department) \
                .join(Permission).join(Address).join(Location).join(Skill). \
                filter(Employee.date_of_birth.between(date1, date2)).all()
        elif department_id != 'No' and (date1 and date2 != ''):
            employees = db.session.query(Employee, Department, Permission, Address, Location, Skill).join(Department) \
                .join(Permission).join(Address).join(Location).join(Skill).\
                filter(Department.id == department_id, Employee.date_of_birth.between(date1, date2)).all()
        elif department_id != 'No' and (date1 == date2 == ''):
            employees = db.session.query(Employee, Department, Permission, Address, Location, Skill).join(Department) \
                .join(Permission).join(Address).join(Location).join(Skill).filter(Department.id == department_id).all()
        else:
            employees = db.session.query(Employee, Department, Permission, Address, Location, Skill).join(Department) \
                .join(Permission).join(Address).join(Location).join(Skill).all()
        for employee, department, permission, address, location, skill in employees:
            user_info = {'name': employee.name, 'surname': employee.surname, 'date_of_birth': employee.date_of_birth,
                         'salary': employee.salary, 'email': employee.email, 'phone': employee.phone,
                         'date_of_joining': employee.date_of_joining, 'department': department.name,
                         'location': location.name, 'work_address': address.name, 'key_skill': skill.name,
                         'permission': permission.name, 'department_id': employee.department,
                         'emp_id': employee.id}
            employee_list.append(user_info)

        return tuple(employee_list)
