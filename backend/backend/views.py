from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.models import User
from rest_framework.permissions import AllowAny
from main.serializers import UserRegisterSerializer
from django.db.utils import IntegrityError

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():
            try:
                user = User.objects.create_user(
                    username=serializer.validated_data['username'],
                    password=serializer.validated_data['password'],
                    role=serializer.validated_data['role']
                )
            except IntegrityError as e:
                if e.args[0].startswith('UNIQUE'):
                    return Response({"error": "Utilisateur existe déjà."}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"error": e.args}, status=status.HTTP_400_BAD_REQUEST)
                
            except Exception as e:
                print(e)

            return Response({"message": f"Utilisateur ({user.role}) {user.username} créé."}, status=status.HTTP_201_CREATED)
        else:
             return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
       