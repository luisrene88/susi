from django.conf.urls import url, include
from django.contrib import admin
from views import ProductoCreateView, KendoListProviderView, ProductoUpdateView, ProductoDeleteView, \
CategoriaViewSet, SubCategoriaViewSet
import views as views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categoria', CategoriaViewSet)
router.register(r'subcategoria', SubCategoriaViewSet)

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="index"),
    url(r'^productos/', views.productos, name="productos"),
    url(r'^contratos/', views.contratos, name="contratos"),
    url(r'^promociones/', views.promociones, name="promociones"),
    url(r'^producto_add/', ProductoCreateView.as_view(), name="producto_add"),
    url(r'^producto_edit/(?P<pk>\d+)/$', ProductoUpdateView.as_view(), name="producto_edit"),
    url(r'^producto_del/(?P<pk>\d+)/$', ProductoDeleteView.as_view(), name="producto_del"),
    url(r'^listado/', KendoListProviderView.as_view(), name="listado"),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]