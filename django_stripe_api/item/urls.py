from django.urls import path

from item.views import show_item, home

urlpatterns = [
    path('item/<int:pk>/', show_item, name='item'),
    path('', home, name='home')
]
