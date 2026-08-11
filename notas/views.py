from django.http import HttpResponse


def inicio(request):
    return HttpResponse("<h1>Notas Colab</h1><p>Tu espacio para pensar.</p>")
