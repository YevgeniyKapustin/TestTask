from django.db.models import F
from django.shortcuts import get_object_or_404

from item.models import Item
from order.models import Order, OrderItem


def get_or_create_order(session_key):
    order = Order.objects.filter(session_key=session_key)
    if not order:
        order = Order.objects.create(session_key=session_key)
    return order[0]


def add_item_to_order(order, item):
    available_order = OrderItem.objects.filter(order=order, item=item)
    if available_order:
        order = available_order.update(quantity=F('quantity')+1)
    else:
        order = OrderItem.objects.create(order=order, item=item)
    return order


def delete_order(order_pk):
    return Order.objects.get(pk=order_pk).delete()


def delete_item_order(request, item_pk):
    order = get_object_or_404(Order, session_key=request.session.session_key)
    item = get_object_or_404(Item, pk=item_pk)
    return OrderItem.objects.get(order=order, item=item).delete()
