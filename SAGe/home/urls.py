from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('', include('cadastro.urls')),
    path('', include('login.urls')),
]