from django.db import models


class Order(models.Model):
    session_key = models.CharField(max_length=50)


class OrderItem(models.Model):
    item = models.ForeignKey('item.Item', on_delete=models.PROTECT)
    order = models.ForeignKey('Order', on_delete=models.PROTECT)