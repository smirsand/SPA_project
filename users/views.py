from django.contrib.auth.hashers import make_password
from rest_framework import generics

from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """
    Контроллер создания пользователя.
    """
    serializer_class = UserSerializer

