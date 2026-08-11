from django.contrib import admin
from django.urls import path

from notas.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
]