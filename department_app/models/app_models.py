"""Models for web-app"""
import datetime
from department_app import db


class Employees(db.Model):
    """Employee table"""
    __tablename__ = 'Employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, default=datetime.date.today())
    salary = db.Column(db.Float, nullable=False)
    phone = db.Column(db.String(13), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    date_of_joining = db.Column(db.Date, default=datetime.date.today(), nullable=False)
    department = db.Column(db.Integer, db.ForeignKey('Department.id'), nullable=False)
    location = db.Column(db.Integer, db.ForeignKey('Locations.id'), nullable=False)
    work_address = db.Column(db.Integer, db.ForeignKey('Addresses.id'), nullable=False)
    key_skill = db.Column(db.Integer, db.ForeignKey('Skills.id'), nullable=False)
    permission = db.Column(db.Integer, db.ForeignKey('Permissions.id'))

    def __init__(self, id, name, surname, department, date_of_birth, salary, phone, email, location,
                 work_address, key_skill, date_of_joining, permission):
        self.id = id
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


class Department(db.Model):
    """Department table"""
    __tablename__ = 'Department'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    manager = db.Column(db.String(100), nullable=False, unique=True)
    date_of_creation = db.Column(db.Date, default=datetime.date.today(), nullable=False)
    department = db.relationship('Employees', backref='Department',
                                 lazy='dynamic')

    def __init__(self, id, name, manager, date_of_creation):
        self.id = id
        self.name = name
        self.manager = manager
        self.date_of_creation = date_of_creation

    def __repr__(self):
        return '<Department: {}>'.format(self.name)


class Locations(db.Model):
    """Locations table"""
    __tablename__ = 'Locations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    location = db.relationship('Employees', backref='Locations',
                               lazy='dynamic')

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return '<Location: {}>'.format(self.name)


class Addresses(db.Model):
    """Addresses table"""
    __tablename__ = 'Addresses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    address = db.relationship('Employees', backref='Addresses',
                              lazy='dynamic')

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return '<Address: {}>'.format(self.name)


class Skills(db.Model):
    """Skills table"""
    __tablename__ = 'Skills'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    skill = db.relationship('Employees', backref='Skills',
                            lazy='dynamic')

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return '<Skill: {}>'.format(self.name)


class Permissions(db.Model):
    """Permissions table"""
    __tablename__ = 'Permissions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    permission = db.relationship('Employees', backref='Permissions',
                                 lazy='dynamic')

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return '<Permission: {}>'.format(self.name)
