import asyncio
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .models import Sales
from .functions import create_user_product, delete_user_product


@receiver(post_save, sender=Sales)
def SendUserProduct(sender, instance, created, **kwargs):
	if instance.userid and instance.is_action:
		try:
			worker={
				"worker_id":instance.user.id,
				"name":instance.user.name,
				"mail":instance.user.mail
			}
			if instance.change_userid:
				instance.userid = instance.change_userid
				instance.change_userid = 0
				delete_product = asyncio.run(delete_user_product(instance.userproductid))

			create_product = asyncio.run(
				create_user_product(
					name=instance.product.name,
					description=instance.product.description,
					daily_amount=instance.product.daily_amount,
					price=instance.product.price,
					number=instance.number,
					user=instance.userid,
					worker=worker
				)
			)
			instance.userproductid = create_product['id']
			instance.is_action = False
			instance.save()
		except:
			pass

	if instance.product.number == 0:
		sale.active = False