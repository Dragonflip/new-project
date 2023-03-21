from django.contrib.auth.models import User
from user.models import Client
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(
            user=instance,
            nome=instance.username
        )

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.client.save()
