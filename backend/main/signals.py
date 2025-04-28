from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Artiste, Proprietaire

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'artists':
            Artiste.objects.create(user=instance)
        elif instance.role == 'concert_owner':
            Proprietaire.objects.create(user=instance)