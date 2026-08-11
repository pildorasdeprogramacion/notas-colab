from django.http import HttpResponse


def inicio(request):
    return HttpResponse("<h1>Mis Notas</h1><p>Tu espacio para pensar.</p>")