"""Model for Employee"""
import datetime
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


@dataclass
class Employee(db.Model):
    """Employees table"""
    id: int
    name: str
    surname: str
    date_of_birth: str
    salary: float
    email: str
    phone: str
    date_of_joining: str
    department: int
    location: int
    work_address: int
    key_skill: int
    permission: int

    __tablename__ = 'Employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.String(50), default=datetime.date.today())
    salary = db.Column(db.Float, nullable=False)
    phone = db.Column(db.String(13), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    date_of_joining = db.Column(db.String(50), default=datetime.date.today(), nullable=False)
    department = db.Column(db.Integer, db.ForeignKey('Department.id'), nullable=False)
    location = db.Column(db.Integer, db.ForeignKey('Location.id'), nullable=False)
    work_address = db.Column(db.Integer, db.ForeignKey('Address.id'), nullable=False)
    key_skill = db.Column(db.Integer, db.ForeignKey('Skill.id'), nullable=False)
    permission = db.Column(db.Integer, db.ForeignKey('Permission.id'))

    def __init__(self, name, surname, department, date_of_birth, salary, phone, email, location,
                 work_address, key_skill, date_of_joining, permission):
        self.name = name
        self.surname = surname
        self.department = department
        self.date_of_birth = date_of_birth
        self.salary = salary
        self.phone = phone
        self.email = email
        self.location = location
        self.work_address = work_address
        self.key_skill = key_skill
        self.date_of_joining = date_of_joining
        self.permission = permission

    def __repr__(self):
        return '<Employee: {}>'.format(self.name)
