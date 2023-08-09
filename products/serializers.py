from collections import OrderedDict
from rest_framework import serializers

from .models import Products, ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = ProductCategory
		fields = ('id','title',)



class ProductSerializer(serializers.ModelSerializer):
	category = ProductCategorySerializer()
	
	class Meta:
		model = Products
		fields = ('id','name','number','by_price','price','discount','active',
						'user','category','media',)

		# read_only_fields = ('id',)

	def to_representation(self, instance):
		data = super().to_representation(instance)
		if data['active']:
			return data

		return OrderedDict()
	

class ProductCreateSerializer(serializers.ModelSerializer):
	active = serializers.BooleanField(default=True)

	class Meta:
		model = Products
		fields = ('id','name','number','by_price','price','discount','active',
			'user','category','media',)

		read_only_fields = ('id',)