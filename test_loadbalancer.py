import pytest
from loadbalancer import loadbalancer


@pytest.fixture
def client():
    with loadbalancer.test_client() as client:
        yield client


def test_host_routing_mango(client):
    result = client.get('/', headers={'Host': 'www.food.com'})
    assert b'This is the food application.' in result.data


def test_host_routing_notfound(client):
    result = client.get('/', headers={'Host': 'www.notfood.com'})
    assert b'Not Found' in result.data
    assert 404 == result.status_code
