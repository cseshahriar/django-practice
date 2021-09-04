from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser
from .models import Buyer

@receiver(post_save, sender=CustomUser)
def post_save_create_buyer(sender, instance, created, **kwargs):
    print('sender: ', sender)
    print('instance: ', instance)
    print('created: ', created)
    if created: # boolean value
        Buyer.objects.create(user=instance)
