from django.urls import path, re_path, include
from . import views

urlpatterns = [
    # Define a URL padrão para o portal, com o ID do paciente
    path('<int:id>/', views.portal_do_paciente, name='portal_do_paciente'), 

    # Define a URL para o cadastro de médicos, com o ID do paciente
    path('<int:id>/cadastro_de_medicos/', views.cadastro_de_medicos, name='cadastro_de_medicos'),

    # Adicione outras URLs aqui, se necessário
]