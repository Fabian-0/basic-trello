from rest_framework.permissions import BasePermission

class UserPermissions(BasePermission):

    def has_permission(self, request, view,):
    
        if request.method == 'GET':
            return False

        if request.method == 'POST' and request.user.is_anonymous:
            return True

        return True

    def has_object_permission(self, request, view, obj):
        print('has object_permission', view, obj)

        if request.method == 'PATCH' and not request.user.is_authenticated:
            return False

        if request.method == 'DELETE':
            return False

        return super().has_object_permission(request, view, obj)


