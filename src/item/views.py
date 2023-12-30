from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from config.settings import STRIPE_PUBLIC_KEY
from item.models import Item
from order.models import OrderItem, Order
from order.services.order import ServiceOrder


def show_item(request: HttpRequest, pk: int) -> render:
    return render(
        request,
        'item/index.html',
        {
            'item': get_object_or_404(Item, pk=pk),
            'public_key': STRIPE_PUBLIC_KEY
        }
    )


def home(request: HttpRequest) -> render:
    order: Order = ServiceOrder.get_or_create(request.session.session_key)
    return render(
        request,
        'item/home.html',
        {
            'items': Item.objects.all(),
            'public_key': STRIPE_PUBLIC_KEY,
            'order_items': OrderItem.objects.filter(order=order),
            'total_price': order.sum_order(),
            'order_pk': order.pk
        }
    )
