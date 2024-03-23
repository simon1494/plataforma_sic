from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    OPERADOR = "operador"
    SUPERVISOR = "supervisor"
    DECISOR = "decisor"
    ADMINISTRADOR = "administrador"
    SIN_ROL = "sin_rol"

    ROL_CHOICES = [
        (OPERADOR, "Operador"),
        (SUPERVISOR, "Supervisor"),
        (DECISOR, "Decisor"),
        (ADMINISTRADOR, "Administrador"),
        (SIN_ROL, "Sin rol"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    dependencia = models.CharField(max_length=100, blank=False, null=False)
    rol = models.CharField(max_length=50, default=SIN_ROL)

    def __str__(self):
        return f"Perfil de {self.user.username}"


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    Profile.objects.create(user=instance)
