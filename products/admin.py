from django.contrib import admin

from .models import Products, ProductCategory

# Register your models here.

@admin.register(Products)
class UsersAdmin(admin.ModelAdmin):
	list_display = ('name','user','active',)
	list_filter = ('name','user','category','active',)



@admin.register(ProductCategory)
class UsersAdmin(admin.ModelAdmin):
	list_display = ('title',)
	list_filter = ('title',)