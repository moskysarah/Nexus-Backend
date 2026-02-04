from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # j'ajoute nos champs XP et Level dans l'affichage de l'admin
    fieldsets = UserAdmin.fieldsets + (
        ('Statistiques RPG', {'fields': ('xp', 'level', 'full_name')}),
    )
    list_display = ['email', 'username', 'xp', 'level', 'is_staff']

admin.site.register(User, CustomUserAdmin)

