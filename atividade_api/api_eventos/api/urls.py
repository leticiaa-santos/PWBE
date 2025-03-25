from django.urls import path
from . import views

#urls para realizar o CRUD, as funções usadas estão nas views
urlpatterns = [
    path('eventos/', views.read_evento),
    path('eventos/criar/', views.create_evento),
    path('eventos/buscar/<int:pk>', views.buscar_evento),
    path('eventos/atualizar/<int:pk>', views.update_evento),
    path('eventos/deletar/<int:pk>', views.delete_evento),
    path('eventos/proximos/', views.ver_proximos),
]