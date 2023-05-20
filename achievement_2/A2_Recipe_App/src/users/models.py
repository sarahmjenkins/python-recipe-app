from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    bio = models.TextField(max_length=250, default='no bio')

    def __str__(self):
        return f'Profile of {self.username}'
