from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    message = 'вы не являетесь модератором'

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False


class IsCreator(BasePermission):
    message = 'вы не являетесь создателем'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.creator:
            return True
        return False
