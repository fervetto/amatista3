from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from apps.productos.views import CrearCategoria


urlpatterns = [
    path('hola', views.decir_hola),
    path('agregar_categoria/', CrearCategoria.as_view(), name='agregar_categoria')
]
 