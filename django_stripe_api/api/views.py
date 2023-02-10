from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from item.models import Item
from item.session import get_stripe_session


class ItemAPIView(viewsets.ViewSet):
    @staticmethod
    def session_id_for_item(request, pk=None):
        item = get_object_or_404(Item, pk=pk)
        session = get_stripe_session(item)
        return Response(session.id)
