"""Location CRUD"""
from sqlalchemy.exc import IntegrityError
from flask import request
from flask_restful import abort
from department_app.database import db
from department_app.models import LocationModel


class CRUDLocation:
    """Location CRUD class"""
    @staticmethod
    def get_location(location_id):
        """Get location func"""
        if not str(location_id).isdigit():
            abort(404, message="ID must be a number.")
        location = LocationModel.query.filter_by(id=location_id).first()
        if not location:
            abort(404, message=f"Could not find location with ID: {location_id}.")
        return location

    @staticmethod
    def get_all_location():
        """Get location func"""
        location_list = []
        locations = LocationModel.query.all()
        if len(locations) > 0:
            for location in locations:
                location_info = {'name': location.name, 'location_id': location.id}
                location_list.append(location_info)
        return tuple(location_list)

    @staticmethod
    def update_location(location_id, json):
        """update location func"""
        location = LocationModel.query.filter_by(id=location_id).first()
        location.name = json['name']

        try:
            db.session.commit()
        except IntegrityError as exception:
            abort(404, message=f"Exception: {exception}")
        return location

    @staticmethod
    def create_location(form=None):
        """Create department func"""
        if form:
            location = LocationModel(name=form.name.data)
        else:
            location = LocationModel(name=request.json['name'])

        try:
            db.session.add(location)
            db.session.commit()
        except IntegrityError as exception:
            abort(404, message=f"Exception: {exception}")
        return location
