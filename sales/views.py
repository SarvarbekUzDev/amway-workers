from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Products
from .models import Sales
from .serializers import SalesSerializer
from .functions import EditProducts


@api_view(['POST'])
def ProductSaleCreateView(request):
	product = request.data.get("product")
	number = request.data.get("number")
	user = request.data.get("user")
	location = request.data.get("location")
	phone = request.data.get("phone")
	userid = request.data.get("userid")
	try:
		EditProducts(product, number, action="del")
		sale = Sales.objects.create(
			number=int(number),
			product_id=int(product),
			user_id=user,
			location=location  if location else '',
			phone=phone  if phone else None,
			userid=userid  if userid else None,
			is_action=True
		)
		serializer = SalesSerializer(sale)
		return Response(serializer.data, status=200)
	except:
		return Response({'error':'Error request.'}, status=400)


@api_view(['POST'])
def ProductUpdateSaleView(request, sale_id):
	number = request.data.get("number")
	product = request.data.get("product")
	userid = request.data.get("userid")
	location = request.data.get("location")
	phone = request.data.get("phone")
	try:
		sale = Sales.objects.get(id=sale_id)
		product_edit = EditProducts(sale.product.id, number, action="add")
		if userid:
			sale.change_userid = sale.userid
		if product:
			sale.product_id = product
		if location:
			sale.location = location
		if number:
			sale.number = number
		if phone:
			sale.phone = phone

		sale.is_action = True
		sale.save()
		return Response({'message':'Product edit'}, status=200)
	except:
		return Response({'error':'Error request.'}, status=400)


@api_view(['DELETE'])
def UserSalesView(request, user_id):
	date = request.data.get("date")
	sales = Sales.objects.filter(
		user_id=user_id,
		date=date
	)
	serializer = SalesSerializer(sales, many=True)
	return Response(serializer.data, status=200)
