from collections import OrderedDict
from rest_framework import serializers

from products.serializers import ProductSerializer
from .models import Sales


class SalesSerializer(serializers.ModelSerializer):
	active = serializers.BooleanField(default=True)
	product = ProductSerializer()

	class Meta:
		model = Sales
		fields = ('id','product','user','number','date','userid','location','active',)

	def to_representation(self, instance):
		data = super().to_representation(instance)
		if data['active']:
			return data

		return OrderedDict()