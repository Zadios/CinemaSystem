from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class FormatAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser', 'last_login')
    search_fields = ('email',)
    list_filter = ('is_active','is_staff', 'is_superuser', 'last_login')

