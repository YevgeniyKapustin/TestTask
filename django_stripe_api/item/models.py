from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    price = models.IntegerField()
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Currency(models.Model):
    abbreviation = models.CharField(max_length=3)
    api_key = models.CharField(max_length=150)
