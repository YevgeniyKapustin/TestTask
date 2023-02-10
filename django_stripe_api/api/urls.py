from django.urls import path

from api.views import ItemAPIView

urlpatterns = [
    path('buy/<int:pk>/', ItemAPIView.as_view({'get': 'session_id_for_item'}),
         name='buy'),
]
