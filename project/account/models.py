from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',)
    profile_pic = models.ImageField(default='default_avatar.png',upload_to='users/', null=True,blank=True)


    def __str__(self):
        return self.user.first_name
    