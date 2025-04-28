# users/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .models import User
from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
@csrf_exempt
def signup(request):
    username = request.data.get('username')
    password = request.data.get('password')
    role = request.data.get('role')

    if role not in ['artiste', 'proprietaire']:
        return Response({'error': 'Rôle invalide'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Utilisateur existe déjà'}, status=400)

    user = User.objects.create_user(username=username, password=password, role=role)
    return Response({'message': 'Utilisateur créé', 'role': user.role})

@api_view(['POST'])
@csrf_exempt
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({'message': 'Connexion réussie', 'role': user.role})
    else:
        return Response({'error': 'Identifiants invalides'}, status=401)

# Middleware basé sur le rôle
def role_required(role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role == role:
                return view_func(request, *args, **kwargs)
            return Response({'error': 'Accès interdit'}, status=403)
        return _wrapped_view
    return decorator

@api_view(['GET'])
@role_required('proprietaire')
def test_proprietaire(request):
    return Response({'message': 'Bienvenue, propriétaire !'})

@api_view(['GET'])
@role_required('artiste')
def test_artiste(request):
    return Response({'message': 'Bienvenue, artiste !'})
