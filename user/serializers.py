from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *
from relative.models import Relative

class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length = 80)
    gender = serializers.CharField(max_length = 1)
    birthdate = serializers.DateField(format="%Y-%m-%d")
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        relative = Relative()
        relative.name = validated_data.pop('name', None)
        relative.gender = validated_data.pop('gender', None)
        relative.birthdate = validated_data.pop('birthdate', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)

        instance.save()
        relative.save()
        return instance
