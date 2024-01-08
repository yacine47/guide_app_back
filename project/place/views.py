from django.shortcuts import render
from rest_framework.decorators import api_view ,permission_classes
from .serializers import PlaceSerializer,CategorySerializer
from .models import Place,Category,Image
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from favorite.models import Favorite

# Create your views here.

# get all Places
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_places(request):
    places = Place.objects.all()
    serializers = PlaceSerializer(places,many=True)
    return Response({
        'places':serializers.data,
    })

# get all categories
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_categories(request):
    categories = Category.objects.all()
    serializers = CategorySerializer(categories,many=True)
    return Response(serializers.data,)


# get all Places
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_places_favorite(request):
    user_profile = request.user 
    favorites = Favorite.objects.filter(id_user =user_profile)
    places_ids = favorites.values_list('id_place',flat=True)
    places = Place.objects.filter(id__in = places_ids)
    serializers = PlaceSerializer(places,many=True)
    return Response(serializers.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Ensure you have the necessary permissions
def add_place_with_images(request):
    place_data = {
        'place_name': request.data.get('place_name'),
        'description': request.data.get('description'),
        'id_state': request.data.get('id_state'),  # Adjust fields as per your model
        'id_category': request.data.get('id_category'),
        'id_user': request.user.id  # Assuming the user is authenticated
    }
    
    place_serializer = PlaceSerializer(data=place_data)
    if place_serializer.is_valid():
        place = place_serializer.save()

        images = request.FILES.getlist('images')
        for image in images:
            Image.objects.create(id_place=place, image=image)
        
        return Response({'message': 'Place added successfully'}, status=201)
    
    return Response(place_serializer.errors, status=400)