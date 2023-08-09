from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UsersSerializer
from .models import Users


class UserCreateView(generics.CreateAPIView):
    # permission_classes = []
    serializer_class = UsersSerializer


class UserUpdateView(generics.UpdateAPIView):
	serializer_class = UsersSerializer

	def put(self, request, id):
		user = get_object_or_404(Users, id=id)
		serializer = self.serializer_class(user, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=200)

		return Response(serializer.errors, status=400)


@api_view(['GET'])
def UserReadView(self, id):
	try:
		user = Users.objects.get(id=id)
		serializer = UsersSerializer(user)
		return Response(serializer.data, status=200)
	except Users.DoesNotExist:
		return Response({'error':"User not found."}, status=404)


@api_view(['POST'])
def UserConformationView(self, id, rand_password):
	try:
		user = Users.objects.get(id=id, rand_password=rand_password)
		user.active = True
		user.save()
		serializer = UsersSerializer(user)
		return Response(serializer.data, status=200)
	except Users.DoesNotExist:
		return Response({'error':"User not found."}, status=404)

