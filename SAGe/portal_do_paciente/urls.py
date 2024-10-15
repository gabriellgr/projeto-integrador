from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path(r'^portal_do_paciente/(?P<id>\d+)/', include([  # Inclui as URLs do 'portal_do_paciente'
        path('', views.portal_do_paciente, name='portal_do_paciente'),  # URL padrão para o portal
        path('atendimento/', views.atendimento, name='atendimento'), 
        path('medicos/', views.medicos, name='medicos'), 
    ])),
]