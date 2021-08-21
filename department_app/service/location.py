"""Location CRUD"""
import logging
from sqlalchemy.exc import IntegrityError

from department_app.models import LocationModel
from department_app.database import db


class CRUDLocation:
    """Location CRUD class"""
    @staticmethod
    def get(location_id):
        """Get location func"""
        logging.info("Get location method called with parameters: id=%s", location_id)

        location = LocationModel.query.filter_by(id=location_id).first()

        if not location:
            return None
        return location

    @staticmethod
    def update(location_id, name):
        """update location func"""
        logging.info("Update location method called with parameters: id=%s, name=%s.", location_id, name)

        try:
            result = LocationModel.query.where(LocationModel.id == location_id). \
                update({LocationModel.name: name})
            db.session.commit()
        except IntegrityError as exception:
            logging.info("Location with name=%s already exist.", name)
            raise exception
        return bool(result)

    @staticmethod
    def get_location_list():
        """Get location func"""
        locations = LocationModel.query.all()

        if len(locations) > 0:
            return tuple(({'name': location.name,
                           'id': location.id} for location in locations))
        return []

    @staticmethod
    def create(name):
        """Create location func"""
        logging.info("Create location method called with parameters: name=%s.", name)

        location = LocationModel(name=name)

        try:
            db.session.add(location)
            db.session.commit()
        except IntegrityError as exception:
            logging.info("Location with name=%s already exist.", name)
            raise exception
        return location
