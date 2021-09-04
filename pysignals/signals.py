from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from users.models import CustomUser
from .models import Buyer, Car
import uuid

@receiver(post_save, sender=CustomUser)
def post_save_create_buyer(sender, instance, created, **kwargs):
    print('sender: ', sender)
    print('instance: ', instance)
    print('created: ', created)
    if created: # boolean value
        Buyer.objects.create(user=instance)


@receiver(pre_save, sender=Car)
def pre_save_modify_buyer_and_create_code(sender, instance, **kwargs):
    if instance.code == "":
        instance.code = str(uuid.uuid4()).replace("-", "").upper()[:10]

    obj = Buyer.objects.get(user=instance.buyer.user)
    obj.from_signal = True
    obj.save()
