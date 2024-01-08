from django.shortcuts import render
from .models import Review
from .serializers import ReviewSerializer,ReviewSerializerAdd
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response 
from rest_framework import status
from place.models import Place
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@api_view(['GET'])
def get_reviews(request):
    reviews = Review.objects.all()
    serializers = ReviewSerializer(reviews,many=True)
    return Response(
        serializers.data,
    )


@api_view(['DELETE'])
def delete_review(request,id):
    try:
        review = Review.objects.get(id=id)
        review.delete()
        return Response({
            'details': 'Review removed successfully',
        }, status=status.HTTP_200_OK)
    except Review.DoesNotExist:
        return Response({
            'details': 'Review does not exist for this user and place',
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_review_place(request):
    data = request.data
    user = request.user 
    review = ReviewSerializerAdd(data=data)
    if review.is_valid():
        if not Review.objects.filter(id_place=data['id_place'], id_user=user).exists():
            review.save(id_user=user)

            return Response({
                    'details':'Review added successfully',
                },status=status.HTTP_201_CREATED)
        else : 
            return Response({
                    'details':'The review is already added',
                },status=status.HTTP_400_BAD_REQUEST)
        
    else :
        return Response(review.errors)
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_reviews_place(request, id_place):
    reviews = Review.objects.filter(id_place=id_place)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)