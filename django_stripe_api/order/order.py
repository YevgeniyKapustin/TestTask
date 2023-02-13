from django.db.models import F

from order.models import Order, OrderItem


def get_or_create_order(session_key):
    order = Order.objects.filter(session_key=session_key)
    if not order:
        order = Order.objects.create(session_key=session_key)[0]
    return order


def add_item_to_order(order, item):
    available_order = OrderItem.objects.filter(order=order, item=item)
    if available_order:
        order = available_order.update(quantity=F('quantity')+1)
    else:
        order = OrderItem.objects.create(order=order, item=item)
    return order
