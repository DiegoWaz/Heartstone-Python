from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    password = models.TextField(max_length=50, blank=True)
    status = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField()

class Card(models.Model):
    name = models.TextField(max_length=50, blank=True)
    description = models.TextField(max_length=500, blank=True)
    cost = models.IntegerField()
    attack_point = models.IntegerField()
    life_point = models.IntegerField()
    type = models.CharField(max_length=10, blank=True)
    classe = models.CharField(max_length=10, blank=True)
    rare = models.CharField(max_length=10, blank=True)
    race = models.CharField(max_length=10, blank=True)
