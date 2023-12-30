"""Model for working with stripe."""
from types import NoneType

import stripe
from django.db.models import QuerySet
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.urls import reverse
from stripe import Customer
from stripe.checkout import Session

from config import settings
from item.models import Currency, Item
from order.models import OrderItem, Order, Discount, Tax


def get_stripe_session_for_item(request: HttpRequest, item: Item) -> Session:
    """Redirect to payment form from stripe for item.
    :returns: Session object.
    """
    set_stripe_api(item)

    line_items: list[dict] = [{
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


def get_stripe_session_for_order(
        request: HttpRequest,
        order_pk: int
) -> Session:
    """Redirect to payment form from stripe for order.
    :returns: Session object.
    """
    set_stripe_api()

    order: Order = get_object_or_404(Order, pk=order_pk)
    order_items: QuerySet = OrderItem.objects.filter(order=order)
    success_url: str = f'/success_buy/{order.pk}/'

    line_items: list = []
    for order_item in order_items:
        item: Item = order_item.item
        item_data: dict = {
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


def create_stripe_session(
        request: HttpRequest,
        line_items: list[dict],
        success_url: str
) -> Session:
    """Creates a session for the purchase
    :returns: Session object."""
    success_absolute_url: str = f'http://{request.get_host()}{success_url}'
    order: Order = Order.objects.filter(
        session_key=request.session.session_key
    )

    if order and Discount.objects.filter(order=order[0]):
        payment_intent = stripe.PaymentIntent.create(
            line_items=line_items,
            amount=amount,
            currency=currency,
            discounts=[{'coupon': create_coupon(request).get('id'), }],
        )
        session: Session = stripe.checkout.Session.create(
            line_items=line_items,
            mode='payment',
            discounts=[{'coupon': create_coupon(request).get('id'), }],
            success_url=success_absolute_url,
        )

    else:
        session: Session = stripe.checkout.Session.create(
            line_items=line_items,
            mode='payment',
            success_url=success_absolute_url,
        )

    return session


def create_coupon(request: HttpRequest, percent_off: int = 20) -> dict:
    """Sets a 20% discount
     :returns: Coupon dict
     """
    order: Order = get_object_or_404(
        Order,
        session_key=request.session.session_key
    )
    Discount.objects.create(order=order, percent_off=percent_off)
    return stripe.Coupon.create(percent_off=percent_off)


def create_tax(request: HttpRequest, country: str = 'RU') -> Customer:
    """Sets the tax for the order
    :returns: Customer stripe object.
    """
    order: Order = get_object_or_404(
        Order,
        session_key=request.session.session_key
    )
    Tax.objects.create(order=order, country=country)

    return stripe.Customer.create(
        description="a new user",
        email="franklin@example.com",
        address={"country": 'RU'},
        expand=["tax"],
    )


def set_stripe_api(item: NoneType | Item = None) -> str:
    """Sets api_key based on the currency.
    If an item is purchased,
    else it takes api_key from the environment.
    :returns: api_key
    """
    if item:
        stripe.api_key = get_object_or_404(
            Currency,
            pk=item.currency.pk
        ).api_key
    else:
        stripe.api_key = settings.STRIPE_API_KEY

    return stripe.api_key
