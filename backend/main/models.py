from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('artist', 'Artist'),
        ('owner', 'ConcertOwner'),
        ('admin', 'Admin')
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    country = models.CharField(max_length=5, null=True, blank=True)

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=255, null=True, blank=True)
    followers = models.IntegerField(default=0, null=True, blank=True)
    
class  ConcertOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adress = models.CharField(null=True, max_length=255, blank=True)
    capacity = models.IntegerField(default=0, blank=True, null=True)

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=255)
    
    rap_hip_hop = models.FloatField(default=0.0)
    pop = models.FloatField(default=0.0)
    electro = models.FloatField(default=0.0)
    rnb = models.FloatField(default=0.0) 
    films_jeux_video = models.FloatField(default=0.0)
    rock_hard_rock = models.FloatField(default=0.0)
    techno_house = models.FloatField(default=0.0)
    country_music = models.FloatField(default=0.0) 
    trance = models.FloatField(default=0.0)
    reggae = models.FloatField(default=0.0)
    
    population_total = models.BigIntegerField(default=0)
    life_expectancy = models.FloatField(default=0.0) 
    birth_rate = models.FloatField(default=0.0)     
    avg_income = models.FloatField(default=0.0)      
