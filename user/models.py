from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Client(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=16)
    endereco = models.CharField(max_length=300)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
