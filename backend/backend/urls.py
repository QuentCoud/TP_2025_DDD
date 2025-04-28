
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='auth_login'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/signup/', RegisterView.as_view(), name='auth_register'),
    path('api/', include('main.urls')),
]
