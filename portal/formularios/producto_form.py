from django import forms
from ..models import Articulos, Propiedades, Imagenes
from django.forms.models import inlineformset_factory
from django.contrib import admin

from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView
from extra_views.generic import GenericInlineFormSet

class ProductoForm(forms.ModelForm):
	class Meta:
		model = Articulos
		fields = '__all__'


class PropiedadesInline(admin.TabularInline):
	model = Propiedades
	extra = 1

class ImagenesInline(admin.TabularInline):
	model = Imagenes
	extra = 1

PropiedadesForm = inlineformset_factory(Articulos, Propiedades, ProductoForm, fields = '__all__', extra=1)
ImagenesForm = inlineformset_factory(Articulos, Imagenes, ProductoForm, fields = '__all__',extra=1)

class PropiedadesInlineForm(InlineFormSet):
	model = Propiedades
	extra = 1
	fields = '__all__'

class ImagenesInlineForm(InlineFormSet):
	model = Imagenes
	extra = 1
	fields = '__all__'