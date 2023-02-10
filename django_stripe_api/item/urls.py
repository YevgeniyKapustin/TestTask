from django.urls import path

from item.views import show_item, redirect_to_first_item

urlpatterns = [
    path('item/<int:pk>/', show_item, name='item'),
    path('', redirect_to_first_item, name='home')
]
