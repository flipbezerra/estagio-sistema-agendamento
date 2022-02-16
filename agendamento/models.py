from django.db import models

# Create your models here.
class Clientes(models.Model):
    nome = models.CharField("Digite seu nome", max_length=200)
    email = models.CharField("Digite seu email", max_length=200)
    telefone = models.CharField("Digite seu telefone", max_length=15, blank=True)
    dataPub = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Events(models.Model):
    title = models.CharField(max_length=50)
    color = models.CharField(max_length=10, default="#FFD700")
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    status = models.BooleanField(default=False)
    dataCadastro = models.DateTimeField(auto_now_add=True)
    # usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
