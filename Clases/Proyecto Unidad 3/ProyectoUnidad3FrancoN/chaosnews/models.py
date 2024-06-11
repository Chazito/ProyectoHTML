from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre_usuario = models.CharField(primary_key=True, max_length=20)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    #Password. Esto solamente para uso academico, no es seguro.
    password = models.CharField()

class 