# users/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from main.permissions import IsArtist, IsConcertOwner
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from main.services import CountriesService, UserService


# dict(request.query_params).update(dict(request.data))


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
    
class CountriesView(APIView):
    permission_classes = [IsArtist]

    def get(self, request, *args, **kwargs):
        return Response(CountriesService.searchCountries(dict(request.query_params)), status=200)
    

class meView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response(UserService.getMe(request.user))