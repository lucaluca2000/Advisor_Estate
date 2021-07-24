from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)

class IsSuperUserOrStaffReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
        	# get access to authors readonly
            request.method in SAFE_METHODS and
            request.user and
            request.user.is_staff or
            # get access to superuser full
            request.user and
            request.user.is_superuser
        )