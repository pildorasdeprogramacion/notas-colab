from django.http import HttpResponse


def inicio(request):
    return HttpResponse("<h1>Notas Colab</h1><p>Organiza tus ideas.</p><footer>Notas Colab 226</footer>")
