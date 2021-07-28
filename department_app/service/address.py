"""Address CRUD"""
from flask import request
from department_app.models.app_models import db, Address


class CRUDAddress:
    """Address CRUD class"""
    @staticmethod
    def get_all_address():
        """Get address func"""
        address_list = []
        addresses = Address.query.all()
        for address in addresses:
            address_info = {'name': address.name, 'address_id': address.id}
            address_list.append(address_info)
        return tuple(address_list)

    @staticmethod
    def create_address():
        """Create department func"""
        form_data = request.form
        address = Address(name=form_data['name'])
        db.session.add(address)
        db.session.commit()
