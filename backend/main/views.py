# users/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from main.permissions import IsArtist, IsConcertOwner
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class PublicView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "Cette route est publique."})
    
class ConcertOwnerView(APIView):
    permission_classes = [IsAuthenticated, IsConcertOwner]

    def get(self, request, *args, **kwargs):
        return Response({"message": "Bienvenue sur la page des concert owners!"})
    
class ArtistView(APIView):
    permission_classes = [IsAuthenticated, IsArtist]

    def get(self, request, *args, **kwargs):
        return Response({"message": "Bienvenue sur la page des artistes!"})

class AllAuthView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({"message": "Bienvenue sur la page des personnes connecté!"})
    
class AdminView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, *args, **kwargs):
        return Response({"message": "Bienvenue sur la page des admin"})