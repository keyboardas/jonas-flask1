"""
Module to test the Flask app
"""

import unittest
from main import app


class TestApp(unittest.TestCase):
    """
    Test cases for the Flask app.
    """

    def setUp(self):
        """
        Set up the test client.
        """
        self.app = app.test_client()

    def test_hello_world(self):
        """
        Test the hello_world route.
        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '<h1><center>This header was changed in a new_branch</center></h1>')


if __name__ == '__main__':
    unittest.main()
