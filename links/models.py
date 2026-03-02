from django.db import models

# Create your models here.

class Tema(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Tema"
        verbose_name_plural = "Temas"

class Recurso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    endereco = models.URLField()
    gratuito = models.BooleanField()
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    data_pub = models.DateField(auto_now_add=True)
    prestigio = models.IntegerField(default=0)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Recurso"
        verbose_name_plural = "Recursos"
    
