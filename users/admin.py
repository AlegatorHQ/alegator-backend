from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    model = User
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('province', 'supabase_id')}),
    )
    list_display = [
        "username",
        "first_name",
        "last_name",
        "email",
        "province",
        "is_staff",
    ]
    search_fields = ["first_name", "last_name", "email", "province", "username"]
    list_filter = ["is_staff", "is_superuser", "is_active", "groups"]

admin.site.register(User, UserAdmin) 