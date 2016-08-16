from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .formularios.producto_form import ProductoForm, PropiedadesForm, ImagenesForm, \
PropiedadesInlineForm, ImagenesInlineForm
from .models import Articulos, Propiedades, Imagenes, Promocion, VistaPromocion, Categoria, SubCategoria
from django.http import HttpResponseRedirect, JsonResponse
from django.forms.models import model_to_dict
from querystring_parser import parser
from django.core.exceptions import FieldError
from django.db.models import Q
import json
from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView, \
InlineFormSetView, NamedFormsetsMixin
from django.views.decorators.gzip import gzip_page
# Create your views here.


@gzip_page
def index(request):
	template = 'index.html'
	context = {}
	return render(request,template,context)
@gzip_page
def productos(request):
	template = 'productos.html'
	context = {}
	return render(request,template,context)
@gzip_page
def contratos(request):
	template = 'contratos.html'
	context = {}
	return render(request,template,context)
@gzip_page
def promociones(request):
	template = 'promociones.html'
	promociones = Promocion.objects.all()
	OWL = VistaPromocion.objects.filter(estatus=True)[0]
	Presentacion = True
	if OWL is None:
		OWL = VistaPromocion.objects.all()[0]
	if OWL is not None:
		if OWL.clave == 'LTA':
			Presentacion = False
	context = {
	'promociones':promociones,
	'OWL':Presentacion
	}
	return render(request,template,context)

class ProductoCreateView(NamedFormsetsMixin, CreateWithInlinesView):
	template_name = 'producto_add.html'
	model = Articulos
	form_class = ProductoForm
	inlines = [PropiedadesInlineForm, ImagenesInlineForm]
	inlines_names = ['propiedades_form', 'imagenes_form']

class ProductoUpdateView(NamedFormsetsMixin, UpdateWithInlinesView):
	template_name = 'producto_add.html'
	model = Articulos
	inlines = [PropiedadesInlineForm, ImagenesInlineForm]
	inlines_names = ['propiedades_form', 'imagenes_form']
	form_class = ProductoForm

class ProductoDeleteView(DeleteView):
	model = Articulos
	template_name = 'producto_del.html'

class ProductoCreateView2(CreateView):
	template_name = 'producto_add.html'
	model = Articulos
	form_class = ProductoForm
	success_url = 'success/'

	def get(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()

		form = self.get_form(form_class)

		propiedades_form = PropiedadesForm()
		imagenes_form = ImagenesForm()

		return self.render_to_response(
			self.get_context_data(
				form=form,
				propiedades_form = propiedades_form,
				imagenes_form = imagenes_form
				)
			)

	def post(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		propiedades_form = PropiedadesForm(request.POST)
		imagenes_form = ImagenesForm(request.POST, request.FILES)
		if (form.is_valid() and imagenes_form.is_valid() and propiedades_form.is_valid()):
			return self.form_valid(form, propiedades_form, imagenes_form)
		else:
			return self.form_invalid(form, propiedades_form, imagenes_form)

	def form_valid(self, form, propiedades_form, imagenes_form):
		self.object = form.save()
		imagenes_form.instance = self.object
		imagenes_form.save()
		propiedades_form.instance = self.object
		propiedades_form.save()
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form, propiedades_form, imagenes_form):
		return self.render_to_response(
			self.get_context_data(
				form=form,
				propiedades_form = propiedades_form,
				imagenes_form = imagenes_form
				)
			)

	

class ProductoUpdateView2(UpdateView):
	template_name = 'producto_add.html'
	model = Articulos
	form_class = ProductoForm
	success_url = 'success/'

	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		form_class = self.get_form_class()

		form = self.get_form(form_class)

		propiedades_form = PropiedadesForm(instance=self.object)
		imagenes_form = ImagenesForm(instance=self.object)

		return self.render_to_response(
			self.get_context_data(
				form=form,
				propiedades_form = propiedades_form,
				imagenes_form = imagenes_form
				)
			)

	def post(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		propiedades_form = PropiedadesForm(request.POST)
		imagenes_form = ImagenesForm(request.POST, request.FILES)
		if (form.is_valid() and imagenes_form.is_valid() and propiedades_form.is_valid()):
			return self.form_valid(form, propiedades_form, imagenes_form)
		else:
			return self.form_invalid(form, propiedades_form, imagenes_form)

	def form_valid(self, form, propiedades_form, imagenes_form):
		self.object= form.save()
		imagenes_form.instance = self.object
		imagenes_form.save()
		propiedades_form.instance = self.object
		propiedades_form.save()
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form, propiedades_form, imagenes_form):
		return self.render_to_response(
			self.get_context_data(
				form=form,
				propiedades_form = propiedades_form,
				imagenes_form = imagenes_form
				)
			)



class KendoListProviderView(ListView):
	filters_ci = True
	distinct = False

	def _build_filters(self, filters, django_filters):
		for filter_id in filters:
			filter = filters[filter_id]
			if(('field' in filter) and ('operator' in filter) and ('value' in filter)):
				if(self.filters_ci and (filter['operator'] == 'startswith' or filter['operator'] == 'endswith'
				or filter['operator'] == 'contains')):
					filter['operator'] = 'i' + filter['operator']

				if "." in filter['field']:
					filter['field'] = filter['field'].replace('.', '__')
					django_filters[filter['field']] = filter['value']
				elif(filter['operator'] == 'eq'):
					django_filters[filter['field']] = filter['value']
				else:
					django_filters[filter['field'] + '__' + filter['operator']] = filter['value']
		return django_filters

	def _build_sorts(self, sorts, django_sorts, append_default_sorting=True):
		for sort_id in sorts:
			sort = sorts[sort_id]
			if(('field' in sort) and ('dir' in sort)):
				if(sort['dir'].lower() == 'desc'):
					django_sorts.append('-%s' % sort['field'])
				else:
					django_sorts.append(sort['field'])
		if(len(django_sorts) == 0):
			django_sorts.append('id')
		return django_sorts

	def _build_groups(self, groups, django_groups):
		return self._build_sorts(groups, django_groups, False)


	def get(self, request, **kwargs):

		arguments = parser.parse(request.GET.urlencode())

		take = int(arguments.get('take', 10))
		skip = int(arguments.get('skip', 0))
		search = str(arguments.get('search', ''))
		subcategoria = str(arguments.get('subcategoria', ''))
		total = skip + take
		filter_arg = dict()
		sort_arg = list()
		filter_logic = 'and'

		if(("filter" in arguments) and ('filters' in arguments['filter'])):
			filter_arg = self._build_filters(arguments['filter']['filters'], filter_arg)
			filter_logic = arguments['filter']['logic'].upper()

		if('group' in arguments):
			sort_arg = self._build_sorts(arguments['group'], sort_arg)

		if('sort' in arguments):
			sort_arg = self._build_sorts(arguments['sort'], sort_arg)

		output = dict()

		try:
			if subcategoria :
				filter_arg['subcategoria__id'] = subcategoria;
			if search :
				filter_arg['nombre__contains'] = search;

			filter_arg['estatus'] = True;

			filters = Q(**filter_arg)
			filters.connector = filter_logic
			#estatus=True,nombre__contains=search
			items = Articulos.objects.filter(filters).order_by(*sort_arg)

			if(self.distinct):
				items = items.distinct()
			self.queryset = items[skip:total]

			datos = self.queryset
			lista = list() 
			for item in datos:
				imgs = list()
				props = list()
				item.img = item.imagenes_set.all().filter(principal=True)
				if len(item.img) is not 0:
					url = str()
					if item.img[0].imagen: 
						url = item.img[0].imagen.url 
					else: 
						url = '#'
					
					itemJson = model_to_dict(item.img[0])
					itemJson['imagen'] = json.dumps(unicode(itemJson['imagen']))
					itemJson['url'] = '%s' % url
					imgs.append(itemJson)
				else:
					item.img = item.imagenes_set.all().filter(principal=False)
					if len(item.img) is not 0:
						url = str()
						#print 'tiene imagen'
						if item.img[0].imagen: 
							url = item.img[0].imagen.url 
						else: 
							url = '#'
						
						itemJson = model_to_dict(item.img[0])
						itemJson['imagen'] = json.dumps(unicode(itemJson['imagen']))
						itemJson['url'] = '%s' % url
						imgs.append(itemJson)
				#for itemImg in item.img:
				#	url = str()
				#	print 'tiene imagen'
				#	if itemImg.imagen: 
				#		url = itemImg.imagen.url 
				#	else: 
				#		url = '#'
					
				#	itemJson = model_to_dict(itemImg)
				#	itemJson['imagen'] = json.dumps(unicode(itemJson['imagen']))
				#	itemJson['url'] = '%s' % url
					#print itemJson['url']
				#	imgs.append(itemJson)

				item.propiedades = item.propiedades_set.all()
				for itemProp in item.propiedades:
					itemJson2 = model_to_dict(itemProp)
					props.append(itemJson2)
				item = model_to_dict(item)
				item['imgs'] = imgs
				item['props'] =  props
				lista.append(item)

			
			output = {'success':True, 'is_authenticated': request.user.is_authenticated(), 
					'Aggregates':{},'Total':items.count(), 'Data' : lista}
		except FieldError:
			output = {'success': False, 'is_authenticated': request.user.is_authenticated(), 
					'Data':'', 'error':'Invalid request. Tried to filter or sort using invalid field.'}

		return JsonResponse(output)


from .serializers.categorias import CategoriaSerializer, SubCategoriaSerializer
from rest_framework import viewsets
from rest_framework import filters

class CategoriaViewSet(viewsets.ModelViewSet):
	queryset = Categoria.objects.filter(estatus=True)
	serializer_class = CategoriaSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('nombre','estatus')


class SubCategoriaViewSet(viewsets.ModelViewSet):
	queryset = SubCategoria.objects.filter(estatus=True)
	serializer_class = SubCategoriaSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('nombre','categoria')