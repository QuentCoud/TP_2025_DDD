from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from main.models import User, Artist, ConcertOwner

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'artist':
            Artist.objects.create(user=instance)
        elif instance.role == 'concert_owner':
            ConcertOwner.objects.create(user=instance)