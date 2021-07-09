from department_app.models.app_models import db
from department_app.models.app_models import Employee


class CRUDEmployee:
    def create(self, name, surname, date_of_birth, salary, email, phone, date_of_joining,
               department, location, work_address, key_skill, permission):
        e = Employee.query.all()
        employee = Employee(id=len(e)+100, name=name, surname=surname, date_of_birth=date_of_birth,
                            salary=salary, email=email, phone=phone, date_of_joining=date_of_joining,
                            department=department, location=location, work_address=work_address,
                            key_skill=key_skill, permission=permission)
        db.session.add(employee)
        db.session.commit()

    def update(self, employee_id, name, surname, date_of_birth, salary, email, phone, date_of_joining,
               department, location, work_address, key_skill, permission):
        employee = Employee.query.filter_by(id=employee_id).first()

        employee.name = name
        employee.surname = surname
        employee.date_of_birth = date_of_birth
        employee.salary = salary
        employee.email = email
        employee.phone = phone
        employee.date_of_joining = date_of_joining
        employee.department = department
        employee.location = location
        employee.work_address = work_address
        employee.key_skill = key_skill
        employee.permission = permission

    def delete(self, employee_id):
        employee = Employee.query.filter_by(id=employee_id).first()
        db.session.delete(employee)
        db.session.commit()

    def get_employee(self, employee_id):
        employee = Employee.query.filter_by(id=employee_id).first()
        return employee

    def search_employee(self, emp_primary_skill):
        employees = Employee.query.filter_by(primary_skill=emp_primary_skill)
        return employees


