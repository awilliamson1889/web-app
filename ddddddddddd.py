from department_app.models.app_models import db, Department, Permission, Address, Location, Skill, Employee
from department_app import create_app
from sqlalchemy.orm import sessionmaker
import sys

Session = sessionmaker()
session = Session()

app = create_app('Test')
app.app_context().push()
#
# # employee_list = []
# # employees = db.session.query(Employee, Department, Permission, Address, Location, Skill).join(Department) \
# #     .join(Permission).join(Address).join(Location).join(Skill).all()
# #
# # for employee, department, permission, address, location, skill in employees:
# #     user_info = {'name': employee.name, 'surname': employee.surname, 'date_of_birth': employee.date_of_birth,
# #                  'salary': employee.salary, 'email': employee.email, 'phone': employee.phone,
# #                  'date_of_joining': employee.date_of_joining, 'department': department.name,
# #                  'location': location.name, 'work_address': address.name, 'key_skill': skill.name,
# #                  'permission': permission.name, 'department_id': employee.department}
# #     employee_list.append(user_info)
# #
# #
# #
# # print(len(employee_list))
# # print(len(tuple(employee_list)))
#
#
# def get_department(department_id):
#     """Get department func"""
#     department_query = Department.query.filter_by(id=department_id).all()
#     for department in department_query:
#         department_info = {'name': department.name, 'manager': department.manager,
#                            'date_of_creation': department.date_of_creation,
#                            'emp_count': len(Employee.query.filter_by(department=department.id).all()),
#                            'dep_id': department.id}
#     return tuple(department_info)
#
# sss = get_department(1)
#
# employee, department = permission = address = location = skill = ''
#
# print(employee)

department_id = 'eeee'
date1 = ' d'
date2 = ' d'


print()
