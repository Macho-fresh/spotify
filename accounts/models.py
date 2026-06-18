from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_artist = models.BooleanField(default=False)
    followers = models.IntegerField(null=True)
    about_artist = models.TextField(max_length=300)

    def __str__(self):
        return self.username