"""Location CRUD"""
from sqlalchemy.exc import IntegrityError
from pydantic import ValidationError
from flask_restful import abort
from flask import request

from department_app.schemas import LocationSchema
from department_app.models import LocationModel
from department_app.database import db
from .service import check_id_format


class CRUDLocation:
    """Location CRUD class"""
    @staticmethod
    def get_location(location_id):
        """Get location func"""
        check_id_format(location_id)

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
    def update_location(location_id):
        """update location func"""
        location = CRUDLocation.get_location(location_id)

        location_data = {'name': location.name}

        location_json = request.json
        location_data.update(location_json)

        try:
            LocationSchema(**location_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        location.name = location_data['name']

        try:
            db.session.commit()
        except IntegrityError as exception:
            abort(404, message=f"Exception: {exception}")
        return location

    @staticmethod
    def create_location(form=None):
        """Create department func"""
        if form:
            location_data = {'name': form.name.data}
        else:
            location_data = {'name': request.json['name']}

        location = LocationModel(**location_data)

        try:
            LocationSchema(**location_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        try:
            db.session.add(location)
            db.session.commit()
        except IntegrityError as exception:
            abort(404, message=f"Exception: {exception}")
        return location
