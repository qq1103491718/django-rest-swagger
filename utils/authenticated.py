from rest_framework.permissions import IsAuthenticated
from utils.pyjwt import jwtencode


class isMyTokenPermission(IsAuthenticated):
    def has_permission(self, request, view):
        token = request.META.get("HTTP_TOKEN")
        return jwtencode().decode(token)
