import stripe
from django.shortcuts import get_object_or_404
from django.urls import reverse

from order.models import OrderItem, Order


def get_stripe_session_for_item(request, item):
    line_items = [{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        },
    ]
    return create_stripe_session(request, line_items, reverse('home'))


def get_stripe_session_for_order(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)
    order_items = OrderItem.objects.filter(order=order)
    line_items = []
    for order_item in order_items:
        item = order_item.item
        item_data = {
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price,
            },
            'quantity': int(order_item.quantity),
        }
        line_items.append(item_data)
    return create_stripe_session(request, line_items,
                                 f'/success_buy/{order.pk}/')


def create_stripe_session(request, line_items, success_url):
    success_absolute_url = f'http://{request.get_host()}{success_url}'

    session = stripe.checkout.Session.create(
        line_items=line_items,
        mode='payment',
        success_url=success_absolute_url,
        )
    return session
