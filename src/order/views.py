from django.shortcuts import redirect, get_object_or_404

from order.models import Order
from item.models import Item
from order.services.stripe import create_coupon, create_tax
from order.services.order import ServiceOrder


def add_to_order(request, item_pk: int) -> redirect:
    if request.method == 'POST':
        order: Order = ServiceOrder.get_or_create(request.session.session_key)
        item: Item = get_object_or_404(Item, pk=item_pk)
        ServiceOrder.add_item(order, item)
    return redirect('home')


def success_buy_order(order_pk: int) -> redirect:
    ServiceOrder.delete(order_pk)
    return redirect('home')


def delete_item_from_order(request, item_pk: int) -> redirect:
    ServiceOrder.delete_item(request, item_pk)
    return redirect('home')


def add_discount(request) -> redirect:
    create_tax(request)
    create_coupon(request)
    return redirect('home')
