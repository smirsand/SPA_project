from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели пользователя.
    """

    def create(self, validated_data):
        password = validated_data['password']  # Пароль из данных сериализатора.
        exemplar = super().create(validated_data)  # Создание экземпляра пользователя
        exemplar.set_password(password)
        exemplar.save()
        return exemplar

    class Meta:
        model = User
        fields = '__all__'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Сериализатор для обработки запросов на получение токена.
    """

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен.
        token['email'] = user.email
        token['first_name'] = user.first_name

        return token
