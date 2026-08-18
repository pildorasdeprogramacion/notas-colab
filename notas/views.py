from django.http import HttpResponse


def inicio(request):
    return HttpResponse("<h1>Notas Colab</h1><p>Tus ideas, en orden</p><footer>Notas Colab 226</footer>")
