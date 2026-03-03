from django.shortcuts import render
from .models import Tema, Recurso

def index(request):
    context = {"lista_temas":Tema.objects.all}
    return render(request, "links/index.html", context) 