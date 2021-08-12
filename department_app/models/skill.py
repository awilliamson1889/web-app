"""Model for Skill"""
from dataclasses import dataclass
from department_app.database import db


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

