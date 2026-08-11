from django.http import HttpResponse


def inicio(request):
    return HttpResponse("<h1>Notas Colab</h1><p>Bienvenido al proyecto.</p>")