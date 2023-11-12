from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Ограничение доступа незарегистрированным пользователям.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_superuser:
            return True

        if request.user == obj.owner:
            return True
        return False
