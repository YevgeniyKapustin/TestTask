from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from item.models import Item
from stripe_logic.stripe_logic import get_stripe_session_for_item, \
    get_stripe_session_for_order


class ItemAPIView(viewsets.ViewSet):
    @staticmethod
    def session_id_for_item(request, item_pk):
        item = get_object_or_404(Item, pk=item_pk)
        session = get_stripe_session_for_item(request, item)
        return Response(session.id)

    @staticmethod
    def session_id_for_order(request, order_pk):
        session = get_stripe_session_for_order(request, order_pk)
        return Response(session.id)
