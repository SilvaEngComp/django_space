from django.db import models

# Create your models here.

class Fotografia(models.Model):
    CATEGORIES=[
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALÁXIA","Gláxia"),
        ("PLANETA","Planeta"),
    ]
        

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria=models.CharField(max_length=100, choices=CATEGORIES, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self) -> str:
        return f" Fotografia [nome={self.nome}]"
    