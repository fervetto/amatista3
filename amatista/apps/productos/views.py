from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from apps.productos.models import Producto, Categoria
from django.contrib.auth.mixins import LoginRequiredMixin
from mixins.custom_test_mixin import CustomTestMixin

# Create your views here.


def decir_hola(request):
    context = {
        'nombre': 'Fernando',
    }
    return render(request, 'hola.html', context)

class CrearCategoria(LoginRequiredMixin, CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'productos/agregar_categoria.html'
    succes_url = reverse_lazy('index')
    
class EliminarCategoria(DeleteView):
    model = Categoria
    template_name = 'genericos/confirma_eliminar.html'
    
class CrearProducto (CreateView, CustomTestMixin):
    model = Producto
    fields = '__all__'
    template_name = 'productos/agregar_producto.html'
    success_url = reverse_lazy('index')
    
    