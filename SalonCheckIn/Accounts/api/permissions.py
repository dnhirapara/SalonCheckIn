from rest_framework import permissions
from rest_framework import exceptions


class SalonUser(permissions.BasePermission):
    """
    Assumed: user already authenticated.
    """

    def has_permission(self, request, view):
        return request.user.is_salon

    def has_object_permission(self, request, view, obj):
        print("permissions: "+str(request.user.is_salon))
        return request.user.is_salon and request.user == obj.user


class SalonUserService(permissions.BasePermission):
    """
    Assumed: user already authenticated.
    """

    def has_permission(self, request, view):
        return request.user.is_salon

    def has_object_permission(self, request, view, obj):
        print("permissions: "+str(request.user.is_salon))
        return request.user.is_salon and request.user == obj.salon.user


class SalonUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.user.is_authenticated)
        if request.method == 'PUT':
            print(request.user)
            if request.user is None:
                print("No user exists")
                return False
                raise exceptions.NotAuthenticated
            else:
                if bool(request.user and request.user.is_authenticated):
                    print("Hello Not User")
                    return request.user.is_salon
                return False
        return True
    # return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_salon and request.user == obj.user
