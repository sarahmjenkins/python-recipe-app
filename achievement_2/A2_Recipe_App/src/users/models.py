from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=12)
    bio = models.TextField(default='no bio')

    def __str__(self):
        return f'Profile of {self.user.username}'
