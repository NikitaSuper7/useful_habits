from rest_framework import permissions


class IsOwnerPermission(permissions.BasePermission):
    """
    Дает право на действие только владельцу привычки.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
