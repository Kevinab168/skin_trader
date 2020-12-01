import factory
from factory.django import DjangoModelFactory

from skin_trader.users import models


class UserFactory(DjangoModelFactory):
    class Meta:
        model = models.User

    username = factory.Faker('user_name')
    password = factory.Faker('password')
