from rest_framework import permissions


class SalonUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'PUT':
            return request.user.is_salon
        return True
    # return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_salon and request.user == obj.user
