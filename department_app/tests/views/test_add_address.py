from unittest.mock import patch
import unittest
from sqlalchemy.exc import IntegrityError

from department_app.app import create_app

app = create_app()
app.app_context().push()


class AddAddressTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()

    def test_add_address_page_get(self):
        with app.test_request_context():
            rv = self.app.get('/add/address')
            self.assertEqual(rv.request.path, '/add/address')
            self.assertEqual(rv.request.method, 'GET')
            self.assertEqual(rv.status_code, 200)

            assert '<title>Add address</title>' in str(rv.data)

    @patch('department_app.views.add_address.CRUDAddress.create')
    def test_add_address_page_post(self, mock_create_address):
        mock_create_address.return_value = {'id': 1,
                                            'name': 'name'}
        with app.test_request_context():
            rv = self.app.post('/add/address', data={'name': 'name'})
            self.assertEqual(rv.request.path, '/add/address')
            self.assertEqual(rv.request.method, 'POST')
            self.assertEqual(rv.status_code, 302)

            assert '<title>Redirecting...</title>' in str(rv.data)

    def test_add_address_page_post_empty_name_field(self):
        with app.test_request_context():
            rv = self.app.post('/add/address')
            self.assertEqual(rv.request.path, '/add/address')
            self.assertEqual(rv.request.method, 'POST')
            self.assertEqual(rv.status_code, 200)

            assert 'This field is required' in str(rv.data)
            assert '<title>Add address</title>' in str(rv.data)

    def test_add_address_page_post_very_long_name(self):
        """Api should return information about address."""
        with app.test_request_context():
            rv = self.app.post('/add/address', data={'name': 'very long name very long name very long name'
                                                             'very long name very long name very long name'
                                                             'very long name very long name very long name'
                                                             'very long name very long name very long name'
                                                             'very long name very long name very long name'})

            assert 'Address length must be between 3 and 100 characters' in str(rv.data)

    @patch('department_app.views.add_address.CRUDAddress.create', side_effect=IntegrityError('', '', ''))
    def test_add_address_page_post_already_exist(self, mock_create):
        """Api should return information about address."""
        with app.test_request_context():
            rv = self.app.post('/add/address', data={'name': 'very long name very long name very long name'})

            assert 'Sorry but this address already exist.' in str(rv.data)
