from django.shortcuts import render
from .models import State
from .serializers import StateSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_states(request):
    states = State.objects.all()
    serializers = StateSerializer(states,many=True)
    return Response(
        serializers.data,
    )