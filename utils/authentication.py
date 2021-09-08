# 校验头部
from user.models import UserProfile
from rest_framework import authentication
from rest_framework import exceptions
from utils.pyjwt import jwtencode
from rest_framework.authentication import BaseAuthentication


class jwtAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get("HTTP_TOKEN")
        pa = jwtencode()
        token
        if not token:
            return None
        # 对token值进行解析
        try:
            pa.decode(encoded=token)
        except Exception as e:
            print(e)


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
