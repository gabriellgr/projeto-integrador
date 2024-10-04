from django.urls import path
from PI_SAGe import views

urlpatterns = [
    path('', views.home, name='home'),  # URL base para a página inicial
    path('portal_do_paciente/', views.portal_do_paciente, name='portal_do_paciente'),
    path('sobre/', views.sobre, name='sobre'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('admin/', views.admin_page, name='admin'),
    path('cadastrar_medicos/', views.cadastrar_medicos, name='cadastrar_medicos'),
    
]