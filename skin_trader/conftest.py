import pytest
from rest_framework.test import APIClient

from skin_trader.users.tests.factories import UserFactory
from skin_trader.items.tests.factories import ItemFactory
from pytest_factoryboy import register

register(UserFactory)
register(ItemFactory)

@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    return UserFactory()
