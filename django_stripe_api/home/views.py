import stripe
from django.shortcuts import render, redirect

from home.get_api import get_session_id_for_item


def index(request):
    print(get_session_id_for_item())
    return render(request, 'home/index.html')


def session_id_for_item(request) -> int:
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'T-shirt',
                },
                'unit_amount': 2000,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/',
    )
    return redirect(session.url, code=303)
