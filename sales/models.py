from django.db import models

from products.models import Products
from users.models import Users


# Create your models here.

class Sales(models.Model):
	number = models.PositiveIntegerField()
	date = models.DateField(auto_now_add=True)
	active = models.BooleanField(default=True)
	is_action = models.BooleanField(default=False)

	userid = models.IntegerField(blank=True, null=True)
	change_userid = models.IntegerField(blank=True, null=True)
	userproductid = models.IntegerField(blank=True, null=True)
	location = models.CharField(max_length=100, blank=True, null=True)
	phone = models.CharField(max_length=15, blank=True, null=True)

	product = models.ForeignKey(Products, on_delete=models.CASCADE)
	user = models.ForeignKey(Users, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.user} | {self.product}"