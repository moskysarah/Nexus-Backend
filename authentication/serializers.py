from rest_framework import serializers
from django.contrib.auth import get_user_model

# On récupère ton modèle User personnalisé
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    # On définit le mot de passe comme "écriture seule" (on ne le renvoie jamais par l'API)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'full_name')

    def create(self, validated_data):
        # On utilise create_user pour hacher le mot de passe automatiquement
        user = User.objects.create_user(
            username=validated_data['email'], # On utilise l'email comme identifiant
            email=validated_data['email'],
            password=validated_data['password'],
            full_name=validated_data.get('full_name', '')
        )
        return user