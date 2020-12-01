import factory
from factory.django import DjangoModelFactory

from skin_trader.items import models


class ItemFactory(DjangoModelFactory):
    class Meta:
        model = models.Item

    name = factory.Faker('name')
    label = factory.Faker('text')
    description = factory.Faker('paragraph')
    price = factory.Faker('random_int')
    game = factory.Faker('word')
    id_number = factory.Faker('ean')
