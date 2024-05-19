from django.db import models
from datetime import datetime

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
    foto = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia=models.DateTimeField(default=datetime.now, blank=False)
    
    def __str__(self) -> str:
        return self.nome
    