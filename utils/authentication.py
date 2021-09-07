# 校验头部
from user.models import UserProfile
from rest_framework import authentication
from rest_framework import exceptions


class ExampleAuthentication(authentication.TokenAuthentication):
    def authenticate(self, request):
        username = request.META.get('X_USERNAME')
        if not username:
            return None

        try:
            user = UserProfile.objects.get(username=username)
        except UserProfile.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)
