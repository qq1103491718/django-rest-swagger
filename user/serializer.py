

from rest_framework import serializers
from .models import UserProfile
from account.serializer import AccountSerializer


class userLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'id']


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    # account = serializers.StringRelatedField(many=True)

    def validate_username(self, validate_username):
        return validate_username

    class Meta:
        model = UserProfile
        fields = ['name', 'birthday', 'gender',
                  'mobile', 'email', 'username', 'id', 'groups']
