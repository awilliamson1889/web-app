"""Address CRUD"""
import logging
from sqlalchemy.exc import IntegrityError

from department_app.models import AddressModel
from department_app.database import db


class CRUDAddress:
    """Address CRUD class"""
    @staticmethod
    def get(address_id: int):
        """Get address func"""
        logging.info("Get method called with parameters: id=%s", address_id)

        return AddressModel.query.filter_by(id=address_id).first()

    @staticmethod
    def update(address_id: int, name: str):
        """update address func"""
        logging.info("Update method called with parameters: id=%s, name=%s.", address_id, name)

        try:
            result = AddressModel.query.where(AddressModel.id == address_id). \
                update({AddressModel.name: name})
            db.session.commit()
        except IntegrityError:
            logging.info("Address with name=%s already exist.", name)
            raise
        return bool(result)

    @staticmethod
    def get_address_list():
        """Get all address func"""
        addresses = AddressModel.query.all()

        if len(addresses) > 0:
            return tuple(({'name': address.name,
                           'id': address.id} for address in addresses))
        return []

    @staticmethod
    def create(name: str):
        """Create address func"""
        logging.info("Create method called with parameters: name=%s.", name)

        address = AddressModel(name=name)

        try:
            db.session.add(address)
            db.session.commit()
        except IntegrityError:
            logging.info("Address with name=%s already exist.", name)
            raise
        return address
