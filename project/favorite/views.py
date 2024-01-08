from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Favorite 
from rest_framework.decorators import api_view , permission_classes
from rest_framework import status
from rest_framework.response import Response 
from .serializers import FavoriteSerializer
from place.models import Place
from place.serializers import PlaceSerializer 
from rest_framework.permissions import IsAuthenticated 


# # Create your views here.




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_favorite_user(request):
    # user = UserSerializer(request.user,many=False)
    user_profile = request.user
    favorites = Favorite.objects.all()
    serializer = FavoriteSerializer(favorites.filter(id_user=user_profile.id),many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_place_favorite(request):
    data = request.data
    user = request.user 
    favorite = FavoriteSerializer(data=data)
    if favorite.is_valid():
        if not Favorite.objects.filter(id_place=data['id_place'], id_user=user).exists():
            favorite.save(id_user=user)

            return Response({
                    'details':'Place added to favorites successfully',
                },status=status.HTTP_201_CREATED)
        else : 
            return Response({
                    'details':'This place is already added',
                },status=status.HTTP_400_BAD_REQUEST)
        
    else :
        return Response(favorite.errors)
    

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_place_favorite(request, place_id):
    user = request.user
    try:
        favorite = Favorite.objects.get(id_place=place_id, id_user=user)
        favorite.delete()
        return Response({
            'details': 'Place removed from favorites successfully',
        }, status=status.HTTP_200_OK)
    except Favorite.DoesNotExist:
        return Response({
            'details': 'Favorite does not exist for this user and place',
        }, status=status.HTTP_404_NOT_FOUND)