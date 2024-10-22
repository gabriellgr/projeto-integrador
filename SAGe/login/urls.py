from django.urls import path
from . import views

urlpatterns = [
    path('', views._login_, name='login'),  #  '/login/'
]