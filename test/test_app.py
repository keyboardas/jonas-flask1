"""
Module to test the Flask app
"""

import pytest
from main import app


@pytest.fixture
def test_client():
    """
    Fixture to set up a test client
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index(test_client):
    """
    Test the index route
    """
    response = test_client.get('/')
    assert b'<h1><center>This header was changed in a new_branch</center></h1>' in response.data


def test_nonexistent_route(test_client):
    """
    Test a nonexistent route
    """
    response = test_client.get('/nonexistent')
    assert response.status_code == 404
