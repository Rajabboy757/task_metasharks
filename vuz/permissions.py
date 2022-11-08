from rest_framework.permissions import BasePermission, IsAuthenticated

from vuz.models import Type


class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.type == Type.admin.value
