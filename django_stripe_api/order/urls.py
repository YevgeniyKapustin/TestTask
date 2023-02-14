from django.urls import path

from order.views import add_to_order, success_buy_order, \
    delete_item_from_order, add_discount

urlpatterns = [
    path('add_item_to_order/<int:item_pk>/', add_to_order,
         name='add_item_to_order'),
    path('success_buy/<int:order_pk>/', success_buy_order,
         name='success_buy_order'),
    path('delete_item_from_order/<int:item_pk>',
         delete_item_from_order, name='delete_item_from_order'),
    path('add_discount', add_discount, name='add_discount'),

]
