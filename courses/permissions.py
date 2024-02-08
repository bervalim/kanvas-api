from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.views import APIView, Request


class IsSuperUser(BasePermission):
    def has_permission(self, request: Request, view: APIView):
        if request.user.is_superuser:
            return True
        return request.method in SAFE_METHODS


class IsSuperUserAndAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser
