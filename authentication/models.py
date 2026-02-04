from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, blank=True)
    
    # --- CHAMPS RPG ---
    xp = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    # Tu pourrais même ajouter :
    # coins = models.IntegerField(default=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email