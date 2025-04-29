from rest_framework import serializers
from main.models import User, Country, Artist, ConcertOwner
from django.contrib.auth import password_validation

class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    role = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'role']
    
    def validate_password(self, value):
        password_validation.validate_password(value)
        return value
    
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role', 'country']

class ArtistSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Artist
        fields = ['user', 'genre', 'followers']


class ConcertOwnerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ConcertOwner
        fields = ['user', 'adress', 'capacity']

class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = User
        fields = ['user']