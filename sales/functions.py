import httpx

from products.models import Products
from data.config import (
	BASE_URL, 
	CREATE_PRODUCT_API_URL,
	DELETE_PRODUCT_API_URL,
	TOKEN,
)


def EditProducts(product_id, number, action):
	product = Products.objects.get(
		id=product_id,
	)
	if action.lower() == "del" and int(product.number) >= int(number) and int(number) > 0:		
		product.number = int(product.number) - int(number)
	elif action.lower() == "add" and int(number) > 0:
		product.number = int(product.number) + int(number)
	else:
		raise ValueError("Error request.")

	product.save()
	return product.number


async def create_user_product(
	name, 
	price, 
	daily_amount, 
	number,
	user,
	worker: dict,
	description=None):
	
	data = {
		"name":name,
		"description":description,
		"price":price,
		"daily_amount":daily_amount,
		"number":number,
		"user":user,
		"worker":{
			"worker_id":worker["worker_id"],
			"name":worker["name"],
			"mail":worker["mail"]
		}
	}
	print(f"{BASE_URL}/{CREATE_PRODUCT_API_URL}","  URL\n\n\n")
	async with httpx.AsyncClient() as client:
		request = await client.post(
							f"{BASE_URL}/{CREATE_PRODUCT_API_URL}",
							json=data,
							headers={"Authorization":f"Token {TOKEN}"})
		return request.json()


async def delete_user_product(product_id):
	async with httpx.AsyncClient() as client:
		request = await client.delete(
						f"{BASE_URL}/{DELETE_PRODUCT_API_URL}/{product_id}",
						headers={"Authorization":f"Token {TOKEN}"})
		return request.json()