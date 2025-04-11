from django.db import models
from django.contrib.auth import User

# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(min_length= 8, max_length= 18)

    def __str__(self):
        return self.username
