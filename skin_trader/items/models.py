from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=60)
    label = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    game = models.CharField(max_length=60)
    id_number = models.IntegerField()

    def __str__(self):
        """Returns string representation."""
        return self.name
