from django.db import models
from django.contrib.auth.models import User
from state.models import *
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=45,default='',)
    icon = models.ImageField(upload_to='category/',null=True)

    def __str__(self):
        return self.category_name
class Place(models.Model):

    place_name = models.CharField(max_length=100,default='')
    description = models.TextField(default='')
    rating = models.DecimalField(max_digits=2, decimal_places=1,default=0)
    number_reviews = models.IntegerField(default=0)
    id_state = models.ForeignKey(State,on_delete=models.CASCADE,null=True,blank=False,related_name='state')
    id_category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=False,related_name='category')
    id_user= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.place_name
    

class Image(models.Model):
    id_place = models.ForeignKey(Place,on_delete=models.CASCADE,null=True,blank=False,related_name='images')
    image = models.ImageField(upload_to='photos/',)

    def __str__(self):
        return self.id_place.place_name

    


