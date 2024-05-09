from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS
# my permissions

class RoomPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.host == request.user
    

class MessagePermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user