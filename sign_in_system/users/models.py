from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('staff', 'Staff'),
        ('community', 'Community Member'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='community')

    def __str__(self):
        return self.username
