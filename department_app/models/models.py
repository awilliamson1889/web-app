"""Model for Address"""
import datetime
from dataclasses import dataclass
from department_app.database import db


@dataclass
class Address(db.Model):
    """Addresses table"""
    id: int
    name: str

    __tablename__ = 'Address'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    address = db.relationship('Employee', backref='Address',
                              lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Address: {}>'.format(self.name)


@dataclass
class Department(db.Model):
    """Departments table"""
    id: int
    name: str
    manager: str
    date_of_creation: str

    __tablename__ = 'Department'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    manager = db.Column(db.String(100), nullable=False)
    date_of_creation = db.Column(db.String(50), default=datetime.date.today())
    department = db.relationship('Employee', backref='Department',
                                 lazy='dynamic')

    def __init__(self, name, manager, date_of_creation):
        self.name = name
        self.manager = manager
        self.date_of_creation = date_of_creation

    def __repr__(self):
        return '<Department: {}>'.format(self.name)


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


@dataclass
class Location(db.Model):
    """Locations table"""
    id: int
    name: str

    __tablename__ = 'Location'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    location = db.relationship('Employee', backref='Location',
                               lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Location: {}>'.format(self.name)


@dataclass
class Permission(db.Model):
    """Permissions table"""
    __tablename__ = 'Permission'
    id: int
    name: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    permission = db.relationship('Employee', backref='Permission',
                                 lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Permission: {}>'.format(self.name)


@dataclass
class Skill(db.Model):
    """Skills table"""
    id: int
    name: str

    __tablename__ = 'Skill'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    skill = db.relationship('Employee', backref='Skill',
                            lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Skill: {}>'.format(self.name)

