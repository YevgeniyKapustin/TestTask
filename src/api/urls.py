from django.urls import path

from api.views import ItemAPIView

urlpatterns = [
    path('buy/<int:item_pk>/', ItemAPIView.as_view({'get': 'session_id_for_item'}),
         name='buy'),
    path('buy_order/<int:order_pk>', ItemAPIView.as_view(
        {'get': 'session_id_for_order'}), name='buy_order')
]
