from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.portal_do_paciente, name='portal_do_paciente'), 
    path('<int:id>/cadastro_de_medicos/', views.cadastro_de_medicos, name='cadastro_de_medicos'),
]