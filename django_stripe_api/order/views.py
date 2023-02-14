from django.shortcuts import redirect, get_object_or_404

from item.models import Item
from item.session import create_coupon
from order.models import OrderItem
from order.order import get_or_create_order, add_item_to_order, delete_order, \
    delete_item_order


def add_to_order(request, item_pk):
    if request.method == 'POST':
        order = get_or_create_order(request.session.session_key)
        item = get_object_or_404(Item, pk=item_pk)
        add_item_to_order(order, item)
    return redirect('home')


def success_buy_order(request, order_pk):
    delete_order(order_pk)
    return redirect('home')


def delete_item_from_order(request, item_pk):
    a = OrderItem.objects.all()
    delete_item_order(request, item_pk)
    return redirect('home')


def add_discount(request):
    create_coupon(request)
    return redirect('home')
