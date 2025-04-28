from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('artiste', 'Artiste'),
        ('proprietaire', 'Propriétaire'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genre = models.JSONField()


class ConcertOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adress = models.CharField(max_length=255)

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)