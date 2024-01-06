from django.db import models
from django.contrib.auth.models import User
from state.models import *
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=45,default='')
    icon = models.ImageField(upload_to='category/',null=True)

class Place(models.Model):
    place_name = models.CharField(max_length=100,default='')
    description = models.TextField(default='')
    rating = models.DecimalField(max_digits=2, decimal_places=1,default=3.0)
    id_state = models.ForeignKey(State,on_delete=models.CASCADE,null=True,blank=False)
    id_category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=False)
    id_user= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=False)
    date = models.DateTimeField(auto_now_add=True)
    

class Image(models.Model):
    id_place = models.ForeignKey(Place,on_delete=models.CASCADE,null=True,blank=False)
    image = models.ImageField(upload_to='photos/',)


