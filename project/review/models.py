from django.db import models
from place.models import Place
from django.contrib.auth.models import User
# Create your models here.


class Review(models.Model):
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    id_place = models.ForeignKey(Place,on_delete=models.CASCADE,null=True,blank=False)
    id_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=False)