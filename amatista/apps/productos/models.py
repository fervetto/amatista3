from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre
    
class Material(models.Model):
    nombre = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=20, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null= True)
    descripción = models.TextField()
    costo = models.FloatField(max_length=10)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True, default='productos/default.png')
    
    def __str__(self):
        return self.nombre