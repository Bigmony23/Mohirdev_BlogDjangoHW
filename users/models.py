from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures',blank=True,null=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'



# Create your models here.
