from django.contrib import admin

from .models import Tournaments, Usertournament


class TournamentsAdmin(admin.ModelAdmin):
    model = Tournaments


class UsertournamentAdmin(admin.ModelAdmin):
    model = Usertournament
    list_display = ["role"]
    search_fields = ["role"]


admin.site.register(Tournaments, TournamentsAdmin)
admin.site.register(Usertournament, UsertournamentAdmin)
