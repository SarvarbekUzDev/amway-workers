import requests as rq
from datetime import datetime as date

BASE_URL = "http://127.0.0.1:80"
TOKEN = "2be1ec53635e5e97e859ff233c5f50cca38bf30e"

# create_user = rq.post(f"{BASE_URL}/api/v1/users/register",
# 				data={
# 					"name":"Name1",
# 					"mail":"Name1@gmail.com",
# 					"password":"123456"},
# 				headers={"Authorization":f"Token {TOKEN}"})


# update_user = rq.put(f"{BASE_URL}/api/v1/users/update/2",
# 				data={
# 					# "name":"Update",
# 					"mail":"Abdulloh@mail.com",
# 					"password":12345678
# 				},
# 				headers={"Authorization":f"TOKEN {TOKEN}"})


# read_user = rq.get(f"{BASE_URL}/api/v1/users/user/12",
# 				headers={"Authorization":f"Token {TOKEN}"})


# confirm_user = rq.post(f"{BASE_URL}/api/v1/users/confirm/12",
# 					headers={"Authorization":f"Token {TOKEN}"})


# print(create_user.json(), create_user)
# print(update_user.json(), update_user)
# print(read_user.json(), read_user)
# print(confirm_user.json(), confirm_user)

# ------------------------- Products ----------------------

# files = [
# 	("media",open("media/products/photo_2023-06-25_08-03-16.jpg","rb"))
# ]

# product_create = rq.post(f"{BASE_URL}/api/v1/products/product/create",
# 					data={
# 						"name":"Vitamin",
# 						"number":25,
# 						"by_price":10000,
# 						"price":11000,
# 						"discount":1000,
# 						"user":2,
# 						"category":1,
# 					},
# 					files=files,
# 					headers={"Authorization":f"Token {TOKEN}"})

# product_read = rq.get(f"{BASE_URL}/api/v1/products/product/1",
# 					headers={"Authorization":f"Token {TOKEN}"})

# user_products = rq.get(f"{BASE_URL}/api/v1/products/user-products/2",
# 						headers={"Authorization":f"token {TOKEN}"})

# product_update = rq.put(f"{BASE_URL}/api/v1/products/product/update/1",
# 						data={
# 							# "name":"Soda | update 1",
# 							# "category":1,
# 							"number":50
# 						},
# 						# files=files,
# 						headers={"Authorization":f"token {TOKEN}"})


# product_delete = rq.delete(f"{BASE_URL}/api/v1/products/product/delete/1",
# 						headers={"Authorization":f"token {TOKEN}"})

# product_categorys = rq.get(f"{BASE_URL}/api/v1/products/product/categorys",
# 						headers={"Authorization":f"token {TOKEN}"})

# print(product_create.json(), product_create)
# print(product_read.json(), product_read)
# print(user_products.json(), user_products)
# print(product_update.json(), product_update)
# print(product_delete.json(), product_delete)
# print(product_categorys.json(), product_categorys)


# --------------------------- Sales -------------------
# create_sale = rq.post(f"{BASE_URL}/api/v1/sales/product/sale/",
# 						data={
# 							"number":2,
# 							"product":2,
# 							"location":"Test lokatsiya",
# 							"user":1,
# 							# "userid":5
# 						},
# 						headers={"Authorization":f"token {TOKEN}"})


# update_sale = rq.post(f"{BASE_URL}/api/v1/sales/update-sale/15",
# 					data={
# 						"number":5,
# 						"location":"Yer shari"
# 					},
# 					headers={"Authorization":f"token {TOKEN}"})

# print(date.today().strftime("%Y-%m-%d").date())
# user_sale = rq.get(f"{BASE_URL}/api/v1/sales/user-sales/1",
# 					data={"date":date.today().strftime("%Y-%m-%d")},
# 					headers={"Authorization":f"token {TOKEN}"})


# print(create_sale.json(), create_sale)
# print(update_sale.json(), update_sale)
# print(user_sale.json())
