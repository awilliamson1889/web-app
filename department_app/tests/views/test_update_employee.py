import unittest

from department_app.app import create_app

app = create_app()
app.app_context().push()


class UpdateEmployeeTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()
