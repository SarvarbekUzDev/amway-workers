from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from random import randint


class UsersManager(BaseUserManager):
	def create_user(self, mail, password, **extra_fields):
		if not mail:
		    raise ValueError(_('Users must have a number address'))
		user = self.model(mail=mail, **extra_fields)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, mail, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
		    raise ValueError(_('Superuser must have is_staff=True.'))
		if extra_fields.get('is_superuser') is not True:
		    raise ValueError(_('Superuser must have is_superuser=True.'))
		return self.create_user(mail, password, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):
	name = models.CharField(max_length=20)
	mail = models.EmailField(max_length=100, unique=True)
	password = models.CharField(max_length=20, validators=[MinLengthValidator(6)])
	rand_password = models.CharField(max_length=5, default=0)
	
	date = models.DateField(auto_now_add=True)
	active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	objects = UsersManager()
	USERNAME_FIELD = 'mail'
	REQUIRED_FIELDS = ('name','password',)
	
	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.rand_password:
			self.rand_password = randint(10000, 99999)

		super(Users, self).save(*args, **kwargs)
