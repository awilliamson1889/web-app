"""Address CRUD"""
from department_app.models.app_models import db, Address


class CRUDAddress:
    """Address CRUD class"""
    @staticmethod
    def get_all_address():
        """Get address func"""
        address_list = []
        addresses = Address.query.all()
        if len(addresses) > 0:
            for address in addresses:
                address_info = {'name': address.name, 'address_id': address.id}
                address_list.append(address_info)
        return tuple(address_list)

    @staticmethod
    def create_address(form):
        """Create address func"""
        address = Address(name=form.name.data)
        db.session.add(address)
        db.session.commit()
        return address
