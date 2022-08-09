from django.urls import path
from PaiApp import views
from .views import Formulario

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('form/',Formulario.as_view(), name="formulario"),
    path('', views.Login, name="login"),
    path('ingresar/', views.ingresar, name="ingresar"),
    path('registrosr/', views.registrosr, name="registrosr"),
]