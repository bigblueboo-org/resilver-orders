from platform_http import Client

from orders.client import load


def test_load():
    assert load(Client("https://api"), "/orders")["url"] == "https://api/orders"


def test_unrelated():
    assert 1 + 1 == 2
