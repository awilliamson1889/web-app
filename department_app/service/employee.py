"""Employee CRUD"""
from flask import request
from department_app.models.app_models import db, Department, Permission, Address, Location, Skill, Employee


class CRUDEmployee:
    """Employee CRUD class"""
    @staticmethod
    def create_employee(form):
        """Create employee func"""
        employee = Employee(name=form.name.data, surname=form.surname.data,
                            date_of_birth=form['date_of_birth'].data, salary=form.salary.data,
                            email=form.email.data, phone=form.phone.data,
                            date_of_joining=form['date_of_joining'].data, department=request.form['department'],
                            location=request.form['location'], work_address=request.form['work_address'],
                            key_skill=request.form['key_skill'], permission=request.form['permission'])
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
    def get_all_employee(department_id='No', date1='', date2='', skill='', name='', location=''):
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
        elif skill != '' and (name == location == ''):
            employees = db.session.query(Employee, Department, Permission, Address, Location, Skill).join(Department) \
                .join(Permission).join(Address).join(Location).join(Skill).filter(Skill.id == skill).all()
        elif location != '' and (name == skill == ''):
            employees = db.session.query(Employee, Department, Permission, Address, Location, Skill).join(Department) \
                .join(Permission).join(Address).join(Location).join(Skill).filter(Location.id == location).all()
        elif ((skill and location) != '') and name == '':
            employees = db.session.query(Employee, Department, Permission, Address, Location, Skill).join(Department) \
                .join(Permission).join(Address).join(Location).join(Skill).filter(Skill.id == skill,
                                                                                  Location.id == location).all()
        elif (skill and location and name) != '':
            employees = db.session.query(Employee, Department, Permission, Address, Location, Skill).join(Department) \
                .join(Permission).join(Address).join(Location).join(Skill).filter(Skill.id == skill,
                                                                                  Location.id == location,
                                                                                  Employee.surname
                                                                                  .like(str('%' + name + '%'))).all()
        elif ((location and name) != '') and skill == '':
            employees = db.session.query(Employee, Department, Permission, Address, Location, Skill).join(Department) \
                .join(Permission).join(Address).join(Location).join(Skill).filter(Location.id == location,
                                                                                  Employee.surname
                                                                                  .like(str('%' + name + '%'))
                                                                                  ).all()
        elif ((skill and name) != '') and location == '':
            employees = db.session.query(Employee, Department, Permission, Address, Location, Skill).join(Department) \
                .join(Permission).join(Address).join(Location).join(Skill).filter(Skill.id == skill,
                                                                                  Employee.surname
                                                                                  .like(str('%' + name + '%'))
                                                                                  ).all()
        elif name != '' and (skill == location == ''):
            employees = db.session.query(Employee, Department, Permission, Address, Location, Skill).join(Department) \
                .join(Permission).join(Address).join(Location).join(Skill).filter(Employee.surname
                                                                                  .like(str('%' + name + '%'))).all()
        else:
            employees = db.session.query(Employee, Department, Permission, Address, Location, Skill).join(Department) \
                .join(Permission).join(Address).join(Location).join(Skill).all()
        for employee, department, permission, address, location_inf, skill_inf in employees:
            user_info = {'name': employee.name, 'surname': employee.surname, 'date_of_birth': employee.date_of_birth,
                         'salary': employee.salary, 'email': employee.email, 'phone': employee.phone,
                         'date_of_joining': employee.date_of_joining, 'department': department.name,
                         'location': location_inf.name, 'work_address': address.name, 'key_skill': skill_inf.name,
                         'permission': permission.name, 'department_id': employee.department,
                         'emp_id': employee.id}
            employee_list.append(user_info)

        return tuple(employee_list)
