from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes # Importé pour gain_xp
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# 1. Inscription
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

# 2. Récupération du profil
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "email": user.email,
            "full_name": user.full_name,
            "xp": user.xp,
            "level": user.level
        })

# 3. Logique de jeu : Gagner de l'XP
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def gain_xp(request):
    user = request.user
    xp_a_ajouter = 10
    
    user.xp += xp_a_ajouter
    
    # Logique de montée de niveau : 
    # Ex: Niveau 2 à 100 XP, Niveau 3 à 200 XP...
    xp_necessaire = user.level * 100
    
    leveled_up = False
    if user.xp >= xp_necessaire:
        user.level += 1
        leveled_up = True
        
    user.save()
    
    return Response({
        "message": "XP ajoutée !",
        "new_xp": user.xp,
        "new_level": user.level,
        "leveled_up": leveled_up
    }, status=status.HTTP_200_OK)