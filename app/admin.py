from django.contrib import admin

from .models import Tournaments


class TournamentsAdmin(admin.ModelAdmin):
    model = Tournaments


admin.site.register(Tournaments, TournamentsAdmin)
