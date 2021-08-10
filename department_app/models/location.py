"""Model for Location"""
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


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
