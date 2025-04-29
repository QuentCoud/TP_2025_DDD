from rest_framework import permissions

class IsArtist(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'artist'
    
class IsConcertOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'concert_owner'
    
class IsAdminOrConcertOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'concert_owner' or request.user.role == 'admin'
    
class IsAdminOrArtist(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'artist' or request.user.role == 'admin'