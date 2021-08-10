"""Address CRUD"""
from department_app.models import db, AddressModel
from flask_restful import abort


class CRUDAddress:
    """Address CRUD class"""
    @staticmethod
    def get_address(address_id):
        """Get all address func"""
        if not str(address_id).isdigit():
            abort(404, message="ID must be a number.")
        address = AddressModel.query.filter_by(id=address_id).first()
        if not address:
            abort(404, message=f"Could not find address with ID: {address_id}.")
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
    def create_address(form):
        """Create address func"""
        address = AddressModel(name=form.name.data)
        db.session.add(address)
        db.session.commit()
        return address