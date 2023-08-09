from django.urls import path

from .views import (
	ProductCreateView,
	ProductReadView,
	UserProductsView,
	ProductUpdateView,
	ProductDeleteView,
	ProductCategorysView
)


urlpatterns = [
	path('product/create', ProductCreateView.as_view(), name='create-product'),
	path('product/<int:product_id>', ProductReadView, name='read-product'),
	path('user-products/<int:user_id>', UserProductsView, name='user-products'),
	path('product/update/<int:product_id>', 
		ProductUpdateView.as_view(), name='update-product'),
	path('product/delete/<int:product_id>',
		ProductDeleteView, name='delete-product'),
	path('product/categorys', ProductCategorysView, name='product-categorys')
]