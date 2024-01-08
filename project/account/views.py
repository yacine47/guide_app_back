from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile 
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view , permission_classes
from rest_framework import status
from rest_framework.response import Response 
from .serializers import SignUpSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated 

# Create your views here.


@api_view(['POST'])
def register(request):
    data = request.data
    user = SignUpSerializer(data=data)
    if user.is_valid() : 
        if not User.objects.filter(username = data['email']).exists():
            user = User.objects.create(  
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email'],
                password = make_password(data['password']),
                username = data['email'],
            )

            return Response({
                'details':'Your account registred successfully',
            },status=status.HTTP_201_CREATED)
        
        else :
            return Response({
                    'details':'This email already exists'
            },status=status.HTTP_400_BAD_REQUEST)
    
    else : 
        return Response(user.errors)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = UserSerializer(request.user,many=False)
    return Response(user.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_profile(request):
    # user = UserSerializer(request.user,many=False)
    user_profile = request.user 
    serializer = UserSerializer(user_profile)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    data = request.data 
    user = request.user 
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.email = data['email']
    user.username = data['email']

    if data['password'] != "": 
        user.password = make_password(data['password'])

    user.save()
    serializer = UserSerializer(user,many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)
