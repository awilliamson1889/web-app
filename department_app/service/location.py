"""Location CRUD"""
from flask import request
from department_app.models.app_models import db, Location


class CRUDLocation:
    """Employee CRUD class"""
    @staticmethod
    def get_all_location():
        """Get location func"""
        location_list = []
        locations = Location.query.all()
        for location in locations:
            location_info = {'name': location.name, 'location_id': location.id}
            location_list.append(location_info)
        return tuple(location_list)

    @staticmethod
    def create_location():
        """Create department func"""
        form_data = request.form
        location = Location(name=form_data['name'])
        db.session.add(location)
        db.session.commit()
