from django.shortcuts import render, get_object_or_404

from django_stripe_api.settings import STRIPE_PUBLIC_KEY
from item.models import Item
from item.session import create_coupon
from order.models import OrderItem
from order.order import get_or_create_order


def show_item(request, pk):
    context = {
        'item': get_object_or_404(Item, pk=pk),
        'public_key': STRIPE_PUBLIC_KEY
    }
    return render(request, 'item/index.html', context)


def home(request):
    order = get_or_create_order(request.session.session_key)

    context = {
        'items': Item.objects.all(),
        'public_key': STRIPE_PUBLIC_KEY,
        'order_items': OrderItem.objects.filter(order=order),
        'total_price': order.sum_order(),
        'order_pk': order.pk
    }
    return render(request, 'item/home.html', context)
