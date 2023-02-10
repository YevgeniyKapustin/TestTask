import stripe
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from item.models import Item


class ItemAPIView(viewsets.ViewSet):
    @staticmethod
    def session_id_for_item(request, pk=None):
        item = get_object_or_404(Item, pk=pk)
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:8000/',
        )
        return Response(session.id)
