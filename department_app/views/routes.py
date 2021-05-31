"""Routes web-app"""
from department_app import app, db
from department_app.models.app_models import Employees

with app.app_context():
    db.create_all()
    db.session.commit()


@app.route('/')
def index():
    return str(Employees.query.all())
