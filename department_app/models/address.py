"""Model for Address"""
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
