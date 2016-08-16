#-*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Articulos, Categoria, SubCategoria, Promocion, VistaPromocion
from .formularios.producto_form import ProductoForm, ImagenesInline, PropiedadesInline 
# Register your models here.

admin.site.site_header = 'Administración de SUSI'

class ArticulosAdmin(admin.ModelAdmin):
	"""docstring for ArticulosAdmin"""
	#change_form_template = 'add_producto.html'
	form = ProductoForm
	list_display = ('nombre','descripcion','subcategoria',)
	search_fields = ('nombre','subcategoria__nombre')
	inlines = [PropiedadesInline, ImagenesInline]
	class Meta:
		model = Articulos
		
class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nombre','estatus')
	class Meta:
		model = Categoria
		
class SubCategoriaAdmin(admin.ModelAdmin):
	list_display = ('nombre','categoria','estatus',)
	search_fields=('nombre','categoria__nombre',)
	class Meta:
		model = SubCategoria

class PromocionAdmin(admin.ModelAdmin):
	list_display= ('nombre','estatus')
	class Meta:
		model = Promocion

class VistaPromocionAdmin(admin.ModelAdmin):
	list_display = ('nombre','clave','estatus')
	list_editable = ('estatus',)
	def has_delete_permission(self, request, obj=None):
		return False
	class Meta:
		model = VistaPromocion
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(SubCategoria, SubCategoriaAdmin)
admin.site.register(Promocion, PromocionAdmin)
admin.site.register(VistaPromocion, VistaPromocionAdmin)