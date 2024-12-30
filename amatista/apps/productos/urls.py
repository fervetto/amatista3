from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from apps.productos.views import CrearCategoria, CrearProducto, CrearMaterial, ProductoView

app_name = 'apps.productos'

urlpatterns = [
    path('hola', views.decir_hola),
    path('agregar_categoria/', CrearCategoria.as_view(), name='agregar_categoria'),
    path('agregar_producto/', CrearProducto.as_view(), name='agregar_producto'),
    path('agregar_material/', CrearMaterial.as_view(), name='agregar_material'),
    path('listar_productos/', ProductoView.as_view(), name='listar_productos')
]
 