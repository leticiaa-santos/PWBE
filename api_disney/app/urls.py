from django.urls import path
from .views import UsuarioListCreateAPIView, IngressoListCreateAPIView, IngressoRUDAPIView, LoginView

urlpatterns = [
    path('usuario/', UsuarioListCreateAPIView.as_view()),
    path('ingresso/', IngressoListCreateAPIView.as_view()),
    path('ingresso/<int:pk>/', IngressoRUDAPIView.as_view()),
    path('login/', LoginView.as_view()),
]