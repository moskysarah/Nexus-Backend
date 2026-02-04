from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, UserDetailView, gain_xp

urlpatterns = [
    # Inscription
    path('register/', RegisterView.as_view(), name='register'),
    
    # Connexion (JWT)
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Profil utilisateur
    path('me/', UserDetailView.as_view(), name='user_me'),
    
    # Action RPG
    path('gain-xp/', gain_xp, name='gain_xp'),
]