from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from apps.productos.models import Producto, Categoria, Material
from django.contrib.auth.mixins import LoginRequiredMixin
from mixins.custom_test_mixin import CustomTestMixin

# Create your views here.


def decir_hola(request):
    context = {
        'nombre': 'Fernando',
    }
    return render(request, 'hola.html', context)
#----------------------------------------- Categoria --------------------------
class CrearCategoria(LoginRequiredMixin, CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'productos/agregar_categoria.html'
    success_url = reverse_lazy('index')
    
   
class EliminarCategoria(DeleteView):
    model = Categoria
    template_name = 'genericos/confirma_eliminar.html'

#---------------- Materiales--------------------------------------------
class CrearMaterial(LoginRequiredMixin, CreateView):
    model = Material
    fields = ['nombre']
    template_name = 'productos/agregar_material.html'
    success_url = reverse_lazy('index')
class EliminarMaterial(DeleteView, CustomTestMixin):
    model = Material
    template_name = 'genericos/confirma_eliminar.html'
    success_url = reverse_lazy('index')
#---------------- Productos---------------------------------------------    
class CrearProducto (CreateView, CustomTestMixin):
    model = Producto
    fields = '__all__'
    template_name = 'productos/agregar_producto.html'
    success_url = reverse_lazy('apps.productos:agregar_producto')
    
class ActualizarProducto(UpdateView, CustomTestMixin):
    model = Producto
    fields = '__all__'
    template_name = 'productos/agregar_producto.html'
    success_url = reverse_lazy('index')
    
class EliminarProducto(DeleteView, CustomTestMixin):
    model = Producto
    template_name = 'genericos/confirma_eliminar.html'
    success_url = reverse_lazy('index')
    
class ProductoView(ListView):
    model = Producto
    template_name = 'productos/listar_productos.html'
    context_object_name = 'productos'