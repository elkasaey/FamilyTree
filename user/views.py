from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenViewBase
from .models import *


class CustomTokenView(TokenViewBase):
    serializer_class = CustomTokenObtainSerializer
    permission_classes = ([AllowAny])

@api_view(['POST'])
def createUser(request):
    serialize = UserSerializer(data=request.data)
    if serialize.is_valid():
        serialize.save()
        return Response(serialize.data,status.HTTP_201_CREATED)
    return Response(serialize.errors,status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getAllGender(request):
    snap = Gender.objects.all()
    serialize = GenderSerializer(snap, many=True)
    return Response(serialize.data,status.HTTP_200_OK)
