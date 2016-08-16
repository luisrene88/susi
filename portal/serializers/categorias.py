from rest_framework import serializers
from ..models import Categoria, SubCategoria

class CategoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categoria
		fields = '__all__'


class SubCategoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = SubCategoria
		fields = '__all__'