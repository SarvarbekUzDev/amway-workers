from django.urls import path

from .views import (
	UserCreateView,
	UserUpdateView,
	UserReadView,
	UserConformationView,
)
from .signals import AdminUserTokenCreate


urlpatterns = [
	path('register', UserCreateView.as_view(), name='register'),
	path('user/<int:id>', UserReadView, name='read-user'),
	path('update/<int:id>', UserUpdateView.as_view(), name='update-user'),
	path('confirm/<int:id>/<int:rand_password>', 
		UserConformationView, name='confirmation-user'),
]