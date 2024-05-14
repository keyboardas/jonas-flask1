import pytest
from main import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get('/')
    assert b'<h1><center>This header was changed in a new_branch</center></h1>' in response.data


def test_nonexistent_route(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
