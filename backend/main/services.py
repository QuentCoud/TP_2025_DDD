from .models import Country, Artist, ConcertOwner, User
from .serializers import CountrySerializer  , ConcertOwnerSerializer, ArtistSerializer, UserSerializer
from .constants import COUNTRY_CODE, GENRE_MAPPING
import json


class UserService:
    def _getModel(self, user):
        if user.role == 'artist':
            model = Artist
        elif user.role == 'owner':
            model = ConcertOwner
        else:
            model = User
        
        return model
    
    def _getSerializer(self, user):
        if user.role == 'artist':
            serializer = ArtistSerializer
        elif user.role == 'owner':
            serializer = ConcertOwnerSerializer
        else:
            serializer = UserSerializer
        
        return serializer

    def _getUserModel(self, user):
        model = self._getModel(user)
        return model.objects.get(id=user.id)

    def getMe(self, user):
        serializer = self._getSerializer(user)
        
        return serializer(self._getUserModel(user)).data
        
    def updateMe(self, user, params):
        allowed_fields = ['genre', 'followers', 'adress', 'capacity']
        user_fields = ['username']

        model = self._getUserModel(user)
        serializer = self._getSerializer(user)

        # TODO REVOIR POUR UPDATE DU GENRE
        
        for field, value in params.items():
            if field in (allowed_fields + user_fields):
                if field in user_fields:
                    setattr(model.user, field, value[0])
                else:
                    if field == 'genre':
                        value = json.dumps(value[0])

                    setattr(model, field, value[0])
        
        model.save()
        return serializer(model).data

class CountriesService:
    def searchCountries(self, filters):
        limit = filters.get('limit', [10])[0]
        genres = filters.get('genres', [])

        if genres:
            genres = genres[0].split(',')
        
        invalid_genres = [g for g in genres if g not in GENRE_MAPPING.values()]

        if invalid_genres:
            raise ValueError(f"Genres invalides : {invalid_genres}")

        genres = [k for k, v in GENRE_MAPPING.items() if v in genres]

        if genres:
            ordering = [f'-{genre}' for genre in genres]
            queryset = Country.objects.all().order_by(*ordering)
        else:
            queryset = Country.objects.all()

        queryset = queryset[:int(limit)]
        serializer = CountrySerializer(queryset, many=True)

        return serializer.data