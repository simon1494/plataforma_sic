from rest_framework.serializers import ModelSerializer
from .models import Profile


class SerializadorProfile(ModelSerializer):
    class Meta:
        model = Profile
        fields = ("nombre", "apellido", "dependencia", "rol")

    def save(self):
        profile = self.validated_data["profile"]
