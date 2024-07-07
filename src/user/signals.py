from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import User
from wallet.models import Wallet


# TODO: This is a bad way
@receiver(post_save, sender=User)
def user_post_save_receiver(sender, instance, created, **kwargs):
    if not created:
        return

    Wallet.objects.create(user=instance)
