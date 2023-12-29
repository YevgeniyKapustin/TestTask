from django.db import models
from django.db.models import QuerySet


class Order(models.Model):
    session_key = models.CharField(max_length=50)

    def __str__(self):
        return f'Order ***{self.session_key[:4:-1]}'

    def sum_order(self):
        items: QuerySet = OrderItem.objects.filter(order=self)
        return sum([item.sum_item() for item in items])


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    item = models.ForeignKey('item.Item', on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} {self.item.name} {self.sum_item()}'

    def sum_item(self):
        return self.item.price * self.quantity


class Discount(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    percent_off = models.IntegerField()

    def __str__(self):
        return f'Discount for {self.order}'


class Tax(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    country = models.CharField(max_length=3)

    def __str__(self):
        return f'Tax for {self.order}'
