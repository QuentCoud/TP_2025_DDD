# users/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from main.permissions import IsArtist, IsConcertOwner, IsAdminOrArtist, IsAdminOrConcertOwner
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from main.services import CountriesService, UserService, ArtistService

class PublicView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "Cette route est publique."})
    
class ConcertOwnerView(APIView):
    permission_classes = [IsConcertOwner]

    def get(self, request, *args, **kwargs):
        return Response({"message": "Bienvenue sur la page des concert owners!"})
    
class ArtistView(APIView):
    permission_classes = [IsArtist]

    def get(self, request, *args, **kwargs):
        return Response({"message": "Bienvenue sur la page des artistes!"})

class AllAuthView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({"message": "Bienvenue sur la page des personnes connecté!"})
    
class AdminView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        return Response({"message": "Bienvenue sur la page des admin"})
    
class CountriesView(APIView):
    permission_classes = [IsAdminOrArtist]

    def get(self, request, *args, **kwargs):
        return Response(CountriesService().searchCountries(dict(request.query_params)), status=200)
    

class meView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response(UserService().getMe(request.user))

    def post(self, request):
        return Response(UserService().updateMe(request.user, dict(request.data)))  

class userAdminView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        return Response(UserService().getAllUsers())

    def post(self, request):
        id = request.data.get('id')
        user = UserService().getUser(id)

        return Response(UserService().updateMe(user, dict(request.data)))  
    
class artistSearchView(APIView):
    permission_classes = [IsAdminOrConcertOwner]

    def get(self, request, *args, **kwargs):
        country = request.query_params.get('country')

        if not country:
            return Response({"error": "Country parameter is required."}, status=400)
        
        return Response(ArtistService().searchArtists(country), status=200)
