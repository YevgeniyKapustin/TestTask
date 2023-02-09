from django.urls import path

from main.views import index, session_id_for_item

urlpatterns = [
    path('', index, name='index'),
    path('session_id_for_item', session_id_for_item, name='session_id_for_item'),
]
