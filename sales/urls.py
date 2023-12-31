from django.urls import path

from .views import (
	ProductSaleCreateView,
	ProductUpdateSaleView,
	ProductSaleDeleteView,
	UserSalesView
)
from .signals import SendUserProduct


urlpatterns = [
	path('product/sale/',
		ProductSaleCreateView, name='sale-product'),
	path('update-sale/<int:sale_id>',
		ProductUpdateSaleView, name='cancel-sale'),
	path('delete-sale/<int:sale_id>',
		ProductSaleDeleteView, name='delete-sale'),
	path('user-sales/<int:user_id>',
		UserSalesView, name='user-sales')
]
