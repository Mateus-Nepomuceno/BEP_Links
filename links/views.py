from django.shortcuts import render, get_object_or_404
from .models import Tema, Recurso

def index(request):
    context = {"lista_temas":Tema.objects.all}
    return render(request, "links/index.html", context) 

def detalhe(request,tema_id):
    tema = get_object_or_404(Tema, pk=tema_id)
    recursos = tema.recurso_set.all().order_by("-prestigio")
    context = {
        "recursos":recursos,
        "tema":tema
    }
    return render(request, "links/detalhe.html", context) 