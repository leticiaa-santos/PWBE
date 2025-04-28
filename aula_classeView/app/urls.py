from django.urls import path
from .views import PilotoListCreateAPIView, CarroListCreateAPIView, PilotoRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('piloto/', view=PilotoListCreateAPIView.as_view()),
    path('carro/', view=CarroListCreateAPIView.as_view()),
    path('piloto/<int:pk>/', view=PilotoRetrieveUpdateDestroyAPIView.as_view()),
]