from .serializers import SerializadorToken
from rest_framework_simplejwt.views import TokenObtainPairView


class ObtenerToken(TokenObtainPairView):
    serializer_class = SerializadorToken
