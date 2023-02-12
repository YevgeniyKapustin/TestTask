from django.shortcuts import redirect, get_object_or_404

from item.models import Item
from item.session import get_stripe_session_for_order
from order.order import get_or_create_order, add_item_to_order


def add_to_order(request, item_pk):
    if request.method == 'POST':
        order = get_or_create_order(request.session.session_key)[0]
        item = get_object_or_404(Item, pk=item_pk)
        add_item_to_order(order, item)
    return redirect('home')


def buy_order(request, order_pk):
    return get_stripe_session_for_order(order_pk)
