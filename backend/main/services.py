from .models import Country, Artist, ConcertOwner, User
from .serializers import CountrySerializer  , ConcertOwnerSerializer, ArtistSerializer, UserSerializer


class UserService:
    def getMe(user):
        if user.role == 'artist':
            model = Artist
            serializer = ArtistSerializer
        elif user.role == 'owner':
            model = ConcertOwner
            serializer = ConcertOwnerSerializer
        else:
            model = User
            serializer = UserSerializer
        
        val = model.objects.get(user=user)
        return serializer(val).data

class CountriesService:
    @staticmethod
    def searchCountries(filters):
        limit = filters.get('limit', 10)
        genres = filters.get('genres', [])

        genres = []
        print(limit, genres)

        return "ok"

        valid_genres = [
            'rap_hip_hop', 'pop', 'electro', 'rnb', 'films_jeux_video',
            'rock_hard_rock', 'techno_house', 'country_music',
            'trance', 'reggae'
        ]
        genres = [g for g in genres if g in valid_genres]

        if genres:
            ordering = [f'-{genre}' for genre in genres]
            queryset = Country.objects.all().order_by(*ordering)
        else:
            queryset = Country.objects.all()

        queryset = queryset[:limit]
        serializer = CountrySerializer(queryset, many=True)

        return serializer.data