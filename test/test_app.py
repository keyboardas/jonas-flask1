"""
Module to test the Flask app
"""

import pytest
from main import app


@pytest.fixture
def client():
    """
    Fixture to set up a test client
    """
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client


def test_index(client):
    """
    Test the index route
    """
    response = client.get('/')
    assert b'<h1><center>This header was changed in a new_branch</center></h1>' in response.data


def test_nonexistent_route(client):
    """
    Test a nonexistent route
    """
    response = client.get('/nonexistent')
    assert response.status_code == 404
