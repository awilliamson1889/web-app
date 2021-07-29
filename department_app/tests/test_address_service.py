import unittest
from department_app import create_app
from department_app.service.address import CRUDAddress
from department_app.models.app_models import Address

app = create_app('Test')
app.app_context().push()


class TestAddressService(unittest.TestCase):
    """ doc str """
    def test_get_all_address_method(self):
        addresses_query = Address.query.all()
        addresses = CRUDAddress.get_all_address()
        addresses_len = len(addresses_query)

        self.assertEqual(addresses_len, len(addresses))



