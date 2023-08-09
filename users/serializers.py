from rest_framework import serializers

from .models import Users


class UsersSerializer(serializers.ModelSerializer):
	active = serializers.BooleanField(default=True)

	class Meta:
		model = Users
		fields = ('id','name','mail','password','active',)

		read_only_fields = ('id',)

	def to_representation(self, instance):
		data = super().to_representation(instance)
		if data['active']:
			return data

		raise serializers.ValidationError("User has no verification.")