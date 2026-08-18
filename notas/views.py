from django.http import HttpResponse
from notas.models import Nota

def inicio(request):
    notas = Nota.objects.count()
    return HttpResponse(
        "<h1>Notas Colab</h1><p>Tus ideas, en orden.</p>"
        f"<p>Notas guardadas: {notas}</p>"
        "<footer>Notas Colab 226</footer>"
    )
