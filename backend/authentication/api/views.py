from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from django.contrib.auth import authenticate

from .serializers import UserSerializer


@api_view(['POST'])
def register_user(request):
    data = request.data
    serializer = UserSerializer(data=data)
    email = data.get('email')
    if not User.objects.filter(email=email).exists():
        serializer.is_valid(raise_exception=True)
        password = data.get('password')
        serializer.save(password=make_password(password))

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({'message': 'A User with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user_detail(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)


# @api_view(['POST'])
# def login(request):
#     data = request.data # { username and password }
#     user = authenticate(username=data.get("username"),
#                         password=data.get("password"))
#     if user is not None:

#         login(request._request, user)
#         return HttpResponse("OK")

#     return HttpResponse("OK")


# def logout(request):
#     logout(request)
#     return Response('')
