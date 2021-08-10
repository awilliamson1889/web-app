"""Model for Department"""
import datetime
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


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
