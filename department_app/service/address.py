"""Address CRUD"""
from sqlalchemy.exc import IntegrityError
from flask import request
from flask_restful import abort
from department_app.database import db
from department_app.models import AddressModel


class CRUDAddress:
    """Address CRUD class"""
    @staticmethod
    def get_address(address_id):
        """Get address func"""
        if not str(address_id).isdigit():
            abort(404, message="ID must be a number.")
        address = AddressModel.query.filter_by(id=address_id).first()
        if not address:
            abort(404, message=f"Could not find address with ID: {address_id}.")
        return address

    @staticmethod
    def update_address(address_id, json):
        """update address func"""
        address = AddressModel.query.filter_by(id=address_id).first()
        address.name = json['name']
        try:
            db.session.commit()
        except IntegrityError as exception:
            abort(404, message=f"Exception: {exception}")
        return address

    @staticmethod
    def get_all_address():
        """Get all address func"""
        address_list = []
        addresses = AddressModel.query.all()
        if len(addresses) > 0:
            for address in addresses:
                address_info = {'name': address.name, 'address_id': address.id}
                address_list.append(address_info)
        return tuple(address_list)

    @staticmethod
    def create_address(form=None):
        """Create address func"""
        if form:
            address = AddressModel(name=form.name.data)
        else:
            address = AddressModel(name=request.json['name'])
        try:
            db.session.add(address)
            db.session.commit()
        except IntegrityError as exception:
            abort(404, message=f"Exception: {exception}")
        return address
