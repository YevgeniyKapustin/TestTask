from django.db import models


class Order(models.Model):
    session_key = models.CharField(max_length=50)

    def sum_order(self):
        items = OrderItem.objects.filter(order=self)
        price = 0
        for i in items:
            price += i.sum_item()
        return price


class OrderItem(models.Model):
    item = models.ForeignKey('item.Item', on_delete=models.PROTECT)
    order = models.ForeignKey('Order', on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} {self.item.name} {self.sum_item()}'

    def sum_item(self):
        return self.item.price * self.quantity
