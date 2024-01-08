from rest_framework import serializers
from .models import Place,Category,Image
from state.serializers import StateSerializer 


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id','image')



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class PlaceSerializer(serializers.ModelSerializer):
    images =  ImageSerializer(many=True,read_only=True)
    state = StateSerializer(many=True,read_only=True) 
    category = CategorySerializer(many=True,read_only=True) 
    class Meta:
        model = Place
        fields = '__all__'


