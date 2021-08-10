from flask_sqlalchemy import SQLAlchemy

from .address import Address as AddressModel
from .department import Department as DepartmentModel
from .employee import Employee as EmployeeModel
from .location import Location as LocationModel
from .permission import Permission as PermissionModel
from .skill import Skill as SkillModel

db = SQLAlchemy()
