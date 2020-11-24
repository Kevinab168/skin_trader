import random
import factory
from factory.django import DjangoModelFactory
from skin_trader.items import models


class ItemFactory(DjangoModelFactory):
    class Meta:
        model = models.Item

    name = factory.Faker('name')
    label = factory.Faker('text')
    description = factory.Faker('paragraph')
    price = random.randint(0, 200)
    game = factory.Faker('word')
    id_number = factory.Faker('ean')
