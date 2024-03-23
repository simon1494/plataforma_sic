from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import obtener_perfil
from .views import actualizar_perfil

urlpatterns = [
    path("ver/", obtener_perfil, name="obtener_perfil"),
    path("actualizar/", actualizar_perfil, name="actualizar_perfil"),
]
