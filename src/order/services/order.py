"""Model for working with orders."""
from django.db.models import F
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from item.models import Item
from order.models import Order, OrderItem


class ServiceOrder(object):
    @staticmethod
    def get_or_create(session_key: str) -> Order:
        """Returns an existing order object by session.
        Else creates a new one for this session.
        :returns: Order object
        """
        order: Order = Order.objects.filter(session_key=session_key)
        return order[0] if order else Order.objects.create(
            session_key=session_key
        )

    @staticmethod
    def add_item(order: Order, item: Item) -> OrderItem:
        """Adds an item to the order.
         if the order is already there, increases its quantity by 1.
         :returns: Order object
         """
        available_order: OrderItem = OrderItem.objects.filter(
            order=order,
            item=item
        )
        if available_order:
            order_item: OrderItem = available_order.update(
                quantity=F('quantity')+1
            )
        else:
            order_item: OrderItem = OrderItem.objects.create(
                order=order,
                item=item
            )
        return order_item

    @staticmethod
    def delete(order_pk: int) -> Order:
        return Order.objects.get(pk=order_pk).delete()

    @staticmethod
    def delete_item(request: HttpRequest, item_pk: int) -> OrderItem:
        order: Order = get_object_or_404(
            Order,
            session_key=request.session.session_key
        )
        item: Item = get_object_or_404(Item, pk=item_pk)
        return OrderItem.objects.get(order=order, item=item).delete()
