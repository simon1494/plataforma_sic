from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("autentificacion/", include("aplicaciones.autentificacion.urls")),
    path("perfiles/", include("aplicaciones.perfiles.urls")),
    path("reunion/", include("aplicaciones.reunion.urls")),
]
