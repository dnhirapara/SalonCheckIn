from rest_framework import permissions
from rest_framework import exceptions


class SalonUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_salon and request.user == obj.user


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
        # elif request.method == 'PATCH' or request.method == 'PUT' or request.method == 'POST' or request.method == 'DELETE':
        #     if request.user is None:
        #         return False
        return request.user.is_salon and request.user == obj.user
