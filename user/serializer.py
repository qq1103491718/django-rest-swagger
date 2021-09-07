
from django.core.validators import validate_email
from rest_framework import serializers
from .models import UserProfile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    def validate_username(self, validate_username):
        return validate_username

    class Meta:

        model = UserProfile
        fields = ['name', 'birthday', 'gender',
                  'mobile', 'email', 'username', 'id', 'groups', 'password']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    '''
    token验证
    '''

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['username'] = self.user.username  # 这个是你的自定义返回的
        data['user_id'] = self.user.id  # 这个是你的自定义返回的

        return data
