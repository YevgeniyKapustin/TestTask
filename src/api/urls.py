from django.urls import path

from .views import ItemAPIView

urlpatterns: list[path] = [
    path(
        'buy/<int:item_pk>/',
        ItemAPIView.as_view({'get': 'session_id_for_item'}),
        name='buy'
    ),
    path(
        'buy_order/<int:order_pk>',
        ItemAPIView.as_view({'get': 'session_id_for_order'}),
        name='buy_order'
    )
]
