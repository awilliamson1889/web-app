"""Address CRUD"""
import logging
from sqlalchemy.exc import IntegrityError, DataError

from department_app.models import AddressModel
from department_app.database import db


class CRUDAddress:
    """Address CRUD class"""
    @staticmethod
    def get(address_id: int):
        """Get address func"""
        logging.info(f"Get method called with parameters: id={address_id}")

        try:
            address = AddressModel.query.filter_by(id=address_id).first()
        except DataError as exception:
            logging.info(f"Address ID={address_id}, has wrong format.")
            raise exception

        if not address:
            return None
        return address

    @staticmethod
    def update(address_id: int, name: str):
        """update address func"""
        logging.info(f"Update method called with parameters: id={address_id}, name={name}.")

        try:
            AddressModel.query.filter(AddressModel.id == address_id). \
                update({AddressModel.name: name}, synchronize_session=False)
            db.session.commit()
        except IntegrityError as exception:
            logging.info(f"Address with name={name} already exist.")
            raise exception
        return {"message": "Data successful updated."}

    @staticmethod
    def get_address_list():
        """Get all address func"""
        addresses = AddressModel.query.all()

        if len(addresses) > 0:
            return tuple(({'name': address.name,
                           'address_id': address.id} for address in addresses))
        return list()

    @staticmethod
    def create(name: str):
        """Create address func"""
        logging.info(f"Create method called with parameters: name={name}.")

        address = AddressModel(name=name)

        try:
            db.session.add(address)
            db.session.commit()
        except IntegrityError as exception:
            logging.info(f"Address with name={name} already exist.")
            raise exception
        return address
