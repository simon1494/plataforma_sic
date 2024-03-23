from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import ObtenerToken

urlpatterns = [
    path("v1/token/", ObtenerToken.as_view()),
    path("v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
