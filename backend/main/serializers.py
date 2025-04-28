from rest_framework import serializers
from main.models import User
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