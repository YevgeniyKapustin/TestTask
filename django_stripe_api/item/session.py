import os

import stripe
from django.shortcuts import get_object_or_404
from django.urls import reverse

from item.models import Currency
from order.models import OrderItem, Order, Discount, Tax


def get_stripe_session_for_item(request, item):
    set_stripe_api(item)

    line_items = [{
            'price_data': {
                'currency': item.currency.abbreviation,
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        }]

    return create_stripe_session(request, line_items, reverse('home'))


def get_stripe_session_for_order(request, order_pk):
    set_stripe_api()

    order = get_object_or_404(Order, pk=order_pk)
    order_items = OrderItem.objects.filter(order=order)
    success_url = f'/success_buy/{order.pk}/'

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

    return create_stripe_session(request, line_items, success_url)


def create_stripe_session(request, line_items, success_url):
    success_absolute_url = f'http://{request.get_host()}{success_url}'
    order = Order.objects.filter(session_key=request.session.session_key)

    if order and Discount.objects.filter(order=order[0]):
        session = stripe.checkout.Session.create(
            line_items=line_items,
            mode='payment',
            discounts=[{'coupon': create_coupon(request).get('id'), }],
            success_url=success_absolute_url,
        )

    else:
        session = stripe.checkout.Session.create(
            line_items=line_items,
            mode='payment',
            success_url=success_absolute_url,
        )
    return session


def create_coupon(request):
    order = get_object_or_404(Order, session_key=request.session.session_key)
    Discount.objects.create(order=order, percent_off=20)

    return stripe.Coupon.create(percent_off=20)


def create_tax(request):
    order = get_object_or_404(Order, session_key=request.session.session_key)
    Tax.objects.create(order=order, country='RU')

    return stripe.Customer.create(
        description="a new user",
        email="franklin@example.com",
        address={"country": 'RU'},
        expand=["tax"],
    )


def set_stripe_api(item=None):
    if item:
        api_key = get_object_or_404(Currency, pk=item.currency.pk).api_key
        stripe.api_key = api_key
    else:
        stripe.api_key = os.getenv('STRIPE_API_KEY')
    return stripe.api_key
