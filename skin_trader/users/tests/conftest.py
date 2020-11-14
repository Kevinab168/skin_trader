import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from skin_trader.users.tests.factories import UserFactory

register(UserFactory)


@pytest.fixture
def api_client():
    return APIClient()
