from __future__ import unicode_literals

from django.db import models
import uuid
import os

from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.sessions.models import Session


# snipper para limpiar cache del sitio cuando se agregue un nuevo dato
@receiver(post_save)
def clear_cache(sender, **kwargs):
	if sender != Session:
		#pass
		cache.clear()

# Create your models here.

choicesMain = (
		('main-start','inicio'),
		('main-center','centro'),
		('main-end','fin'),
	)

choicesCross = (
		('cross-start','inicio'),
		('cross-center','centro'),
		('cross-end','fin'),
	)

class Categoria(models.Model):
	nombre= models.CharField(max_length=150,null=False, blank=False)
	estatus= models.BooleanField(default=True)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name='Categoria'
		verbose_name_plural='Categorias'

class SubCategoria(models.Model):
	categoria = models.ForeignKey(Categoria, null=False, on_delete= models.CASCADE)
	nombre= models.CharField(max_length=150,null=False, blank=False)
	estatus= models.BooleanField(default=True)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name='Sub Categoria'
		verbose_name_plural='Sub Categorias'
	

class Articulos(models.Model):
	"""docstring for Articulos"""
	subcategoria = models.ForeignKey(SubCategoria,null=True)
	nombre = models.CharField(max_length=150, null=False, blank=False)
	descripcion = models.TextField(max_length=350, null=False, blank=False)
	estatus=models.BooleanField(default=True)

	def __str__(self):
		return self.nombre

	def obtener_imagenes(self):
		result = Imagenes.objects.filter(articulos=self);

	class Meta:
		verbose_name='Articulo'
		verbose_name_plural='Articulos'

class Propiedades(models.Model):
	articulo = models.ForeignKey(Articulos, on_delete= models.CASCADE)
	propiedad = models.CharField(max_length=150, null=False, blank=False)
	propiedad.verbose_name= 'Especificacion'

	def __str__(self):
		return self.propiedad

	class Meta:
		verbose_name='Especificacion'
		verbose_name_plural='Especificaciones'

class Imagenes(models.Model):
	articulo = models.ForeignKey(Articulos, on_delete= models.CASCADE)
	imagen = models.ImageField(upload_to='img_articulos', verbose_name="Imagen",
                                     null=True, blank=True)
	principal = models.BooleanField(default=False)
	class Meta:
		verbose_name='Imagen'
		verbose_name_plural='Imagenes'

class Promocion(models.Model):
	nombre = models.CharField(max_length=150, null=False)
	descripcion = models.TextField(max_length=350, blank=True, null=True)
	imagen = models.ImageField(upload_to='img_promo',null=True, blank=True)
	archivo = models.FileField(upload_to='img_promo',null=True, blank=True)
	alineamientox = models.CharField(max_length=15,choices=choicesMain)
	alineamientoy = models.CharField(max_length=15,choices=choicesCross)
	estatus = models.BooleanField(default=True)
	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name='Promocion'
		verbose_name_plural='Promociones'


class VistaPromocion(models.Model):
	nombre = models.CharField(max_length=150, null=False)
	clave = models.CharField(max_length=5, null=False)
	estatus = models.BooleanField(default=True)
	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name='Vista de Promocion'
		verbose_name_plural = 'Vista de Promociones'

		