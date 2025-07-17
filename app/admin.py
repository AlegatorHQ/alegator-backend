from django.contrib import admin

from .models import Tournaments, Usertournament, Users

class UserAdmin(admin.ModelAdmin):
    model = Users
    list_display = ["first_name", "last_name", "email", "province", "is_active", "is_staff", "is_superuser"]
    search_fields = ["first_name", "last_name", "email", "province"]
    list_filter = ["is_active", "is_staff", "is_superuser"]

class TournamentsAdmin(admin.ModelAdmin):
    model = Tournaments


class UsertournamentAdmin(admin.ModelAdmin):
    model = Usertournament
    list_display = ["role"]
    search_fields = ["role"]


admin.site.register(Users, UserAdmin)
admin.site.register(Tournaments, TournamentsAdmin)
admin.site.register(Usertournament, UsertournamentAdmin)
