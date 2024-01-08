from django.db import models
from django.contrib.auth.models import User
from place.models import Place

# Create your models here.


class Favorite(models.Model):
    id_place = models.ForeignKey(Place,on_delete=models.CASCADE,null=True,blank=False)
    id_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=False)

    def __str__(self):
        return self.id_place.place_name
    
    