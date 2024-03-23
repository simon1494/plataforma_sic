from rest_framework.response import Response
from .serializers import SerializadorProfile
from .models import Profile
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def obtener_perfil(request, *args, **kwargs):
    user = request.user
    profile = Profile.objects.get(user=user)
    serializer = SerializadorProfile(profile)

    return Response(serializer)


@api_view(["UPDATE"])
@permission_classes([IsAuthenticated])
def actualizar_perfil(request, *args, **kwargs):
    user = request.user
    profile = Profile.objects.get(user=user)
    data = request.data

    profile.nombre = data.nombre if data.nombre else None
    profile.apellido = data.apellido if data.apellido else None
    profile.dependencia = data.dependencia if data.dependencia else None

    return Response("Perfil actualizado", status=200)
