
from django.core.validators import validate_email
from rest_framework import serializers
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    def validate_username(self, validate_username):
        return validate_username

    class Meta:

        model = UserProfile
        fields = ['name', 'birthday', 'gender',
                  'mobile', 'email', 'username', 'id', 'groups', 'password']
