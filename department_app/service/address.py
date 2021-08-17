"""Address CRUD"""
from sqlalchemy.exc import IntegrityError, DataError

from department_app.models import AddressModel
from department_app.database import db


class CRUDAddress:
    """Address CRUD class"""
    @staticmethod
    def get(address_id: int):
        """Get address func"""
        try:
            address = AddressModel.query.filter_by(id=address_id).first()
        except DataError as exception:
            raise exception

        if not address:
            return None
        return address

    @staticmethod
    def update(address_id: int, name: str):
        """update address func"""
        address = CRUDAddress.get(address_id)

        address.name = name

        try:
            db.session.commit()
        except IntegrityError as exception:
            raise exception
        return address

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
        address = AddressModel(name=name)

        try:
            db.session.add(address)
            db.session.commit()
        except IntegrityError as exception:
            raise exception
        return address
