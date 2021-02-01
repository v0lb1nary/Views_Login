from django.db import models
from django.contrib.auth import auth



class Cliente(models.Model):

    name = models.CharField(max_length=50) 
    login = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("cliente")
        verbose_name_plural = ("clientes")

    def __str__(self):
        return self.name

    