from django.urls import path
from PaiApp import views
from .views import Cierremensual, Formsr, Maestroins

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('maestroins/',Maestroins.as_view(), name="maestroins"),
    path('cierremensual/',Cierremensual.as_view(), name="cierremensual"),
    path('formsr/',Formsr.as_view(), name="formulariosr"),
    path('', views.login, name="login"),
    path('ingresar/', views.ingresar, name="ingresar"),
    path('registrosr/', views.registrosr, name="registrosr"),
]