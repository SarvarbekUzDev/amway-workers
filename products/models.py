from django.db import models

from users.models import Users

# Create your models here.

class ProductCategory(models.Model):
	title = models.CharField(max_length=20)

	def __str__(self):
		return self.title

class Products(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(max_length=150, blank=True, null=True)
	number = models.PositiveIntegerField()
	by_price = models.FloatField()
	price  = models.FloatField()
	discount = models.PositiveIntegerField(default=0)
	daily_amount = models.PositiveIntegerField(blank=True, null=True)
	date = models.DateField(auto_now_add=True)
	active = models.BooleanField(default=True)

	category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
	media = models.ImageField(upload_to='products/', blank=True, null=True)
	user = models.ForeignKey(Users, on_delete=models.CASCADE)

	def __str__(self):
		return self.name