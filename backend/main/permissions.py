from rest_framework import permissions

class IsArtist(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'artist'
    
class IsConcertOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'concert_owner'