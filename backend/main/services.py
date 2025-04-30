from .models import Country, Artist, ConcertOwner, User, Admin
from .serializers import CountrySerializer  , ConcertOwnerSerializer, ArtistSerializer, UserSerializer, AdminSerializer
from .constants import COUNTRY_CODE, GENRE_MAPPING


class UserService:
    def _getModel(self, user):
        if user.role == 'artist':
            model = Artist
        elif user.role == 'owner':
            model = ConcertOwner
        elif user.role == 'admin':
            model = Admin
        else:
            model = User
        
        return model
    
    def _getSerializer(self, user):
        if user.role == 'artist':
            serializer = ArtistSerializer
        elif user.role == 'owner':
            serializer = ConcertOwnerSerializer
        elif user.role == 'admin':
            serializer = AdminSerializer
        else:
            serializer = UserSerializer
        
        return serializer

    def _getUserModel(self, user):
        model = self._getModel(user)
        return model.objects.get(user__id=user.id)

    def getMe(self, user):
        serializer = self._getSerializer(user)
        model = self._getUserModel(user)

        return serializer(model).data

    def getUser(self, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return None
        
        return user
    
    def getAllUsers(self):
        queryset = User.objects.exclude(role='admin')
        serializer = UserSerializer(queryset, many=True)
        
        return serializer.data

    def updateMe(self, user, params):
        allowed_fields = ['genre', 'followers', 'adress', 'capacity']
        user_fields = ['username', 'country']

        model = self._getUserModel(user)
        serializer = self._getSerializer(user)

        user_data = params.get('user', {})

        for field in user_fields:
            if field in user_data:
                setattr(model.user, field, user_data[field])

        for field in allowed_fields:
            if field in params:
                setattr(model, field, params[field])

        model.user.save()
        model.save()

        return serializer(model).data


class CountriesService:
    def searchCountries(self, filters):
        limit = filters.get('limit', [10])[0]
        genre = filters.get('genres', [])
        
        if len(genre) > 0:
            genre = genre[0]
        
        if not genre in GENRE_MAPPING.values():
            raise ValueError(f"Genres invalides : {genre}")

        genre = [k for k, v in GENRE_MAPPING.items() if v == genre][0]

        if genre:
            queryset = Country.objects.all().order_by(f'-{genre}')
        else:
            queryset = Country.objects.all()

        queryset = queryset[:int(limit)]
        serializer = CountrySerializer(queryset, many=True)

        return serializer.data
    

class ArtistService:
    def searchArtists(self, country_code):
        artists = Artist.objects.filter(user__country=country_code).order_by('-followers')
        serializer = ArtistSerializer(artists, many=True)

        return serializer.data