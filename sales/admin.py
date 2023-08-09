from django.contrib import admin

from .models import Sales

# Register your models here.
@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
	list_display = ('product','date','active',)
	list_filter = ('product','date','active',)