import unittest
from department_app import create_app
from department_app.service.location import CRUDLocation
from department_app.models.app_models import Location

app = create_app('Test')
app.app_context().push()


class TestLocationService(unittest.TestCase):
    """ doc str """
    def test_get_all_location_method(self):
        locations_query = Location.query.all()
        locations = CRUDLocation.get_all_location()
        location_len = len(locations_query)

        self.assertEqual(location_len, len(locations))
