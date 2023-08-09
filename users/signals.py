from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token

from .models import Users


@receiver(post_save, sender=Users)
def AdminUserTokenCreate(sender, instance, created, **kwargs):
	if created and instance.is_superuser:
		print("TOKEN CREATED ...", instance)
		token = Token.objects.create(user=instance)