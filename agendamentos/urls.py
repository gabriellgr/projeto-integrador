from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.agendar_consulta, name='agendar_consulta'),
]