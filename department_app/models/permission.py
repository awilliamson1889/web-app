"""Model for Permission"""
from dataclasses import dataclass
from department_app.database import db


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
