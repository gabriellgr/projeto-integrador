from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.portal_do_paciente, name='portal_do_paciente'),  # Note: '<int:id>' agora é o primeiro segmento
]