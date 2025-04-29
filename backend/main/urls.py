from django.urls import path
from .views import PublicView, ArtistView, ConcertOwnerView, AllAuthView, AdminView, CountriesView, meView, userAdminView, artistSearchView

urlpatterns = [
    path('public', PublicView.as_view(), name='public_view'),
    path('concert_owner', ConcertOwnerView.as_view(), name='concert_owner_view'),
    path('artist', ArtistView.as_view(), name='artist_view'),
    path('authenticated', AllAuthView.as_view(), name='all_authenticated_view'),
    path('admin', AdminView.as_view(), name='admin_view'),
    path('me', meView.as_view(), name='me_view'),
    path('countries', CountriesView.as_view(), name='countries_view'),
    path('user', userAdminView.as_view(), name='user_admin_view'),
    path('artist/search', artistSearchView.as_view(), name='artist_search_view'),
]