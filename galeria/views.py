from django.shortcuts import render
from django.http import HttpResponse
from pathlib import os

def index(request):
    return render(request,'galeria/index.html')

def imagem(request):
    return render(request,'galeria/imagem.html')
    