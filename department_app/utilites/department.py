"""Department dataclass module"""
from dataclasses import dataclass

from department_app.models import EmployeeModel


@dataclass
class Department:
    """Department dataclass"""
    name: str
    manager: str
    date_of_creation: str
    employees: int
    department_avg_salary: float
    department_id: int

    @staticmethod
    def convert_db_to_entity(department):
        """Method to convert db to entity"""
        if not department:
            return None
        employee = EmployeeModel.query.filter_by(department=department.id).all()

        dep = Department(name=department.name,
                         manager=department.manager,
                         date_of_creation=department.date_of_creation,
                         employees=EmployeeModel.query.filter_by(department=department.id).count(),
                         department_avg_salary=sum([x.salary for x in employee]),
                         department_id=department.id)
        return dep
