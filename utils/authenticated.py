from rest_framework.permissions import BasePermission
from utils.pyjwt import jwtencode


class isMyTokenPermission(BasePermission):
    def has_permission(self, request, view):
        token = request.META.get("HTTP_TOKEN")
        return bool(token)
