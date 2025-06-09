from django.urls import path
from .views import (
    SensoresListCreate,
    SensoresRetrieveUpdateDestroy,
    AmbienteListCreate,
    AmbienteRetrieveUpdateDestroy,
    HistoricoListCreate,
    HistoricoRetrieveUpdateDestroy,
    ImportarExcel,
    ExportarExcel,
    exportar_excel
)
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    # Login
    path('login/', TokenObtainPairView.as_view()), 

    # Sensores
    path('sensores/', SensoresListCreate.as_view()),
    path('sensores/<int:pk>/', SensoresRetrieveUpdateDestroy.as_view()),

    # Ambientes
    path('ambientes/', AmbienteListCreate.as_view()),
    path('ambientes/<int:pk>/', AmbienteRetrieveUpdateDestroy.as_view()),

    # Historico
    path('historico/', HistoricoListCreate.as_view()),
    path('historico/<int:pk>/', HistoricoRetrieveUpdateDestroy.as_view()),

    # Excel
    path('importar/', ImportarExcel.as_view()),
    path('exportar/', ExportarExcel.as_view()),
    # path('exportar/', exportar_excel, name='exportar_excel'),
]