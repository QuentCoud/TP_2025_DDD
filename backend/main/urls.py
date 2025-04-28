from django.urls import path
from main import views

urlpatterns = [
    path('signup', views.signup),
    path('login', views.login_view),
    path('test-proprietaire', views.test_proprietaire),
    path('test-artist', views.test_artiste)
]