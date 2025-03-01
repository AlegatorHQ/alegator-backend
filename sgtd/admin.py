from django.contrib import admin

from .models import (
    Adjudicators,
    Draws,
    DrawsAdjudicators,
    Rounds,
    SpeakerResults,
    Speakers,
    TeamResults,
    Teams,
)


class AdjudicatorsAdmin(admin.ModelAdmin):
    model = Adjudicators
    list_display = ["name"]
    search_fields = ["name"]


class DrawsAdmin(admin.ModelAdmin):
    model = Draws


class DrawsAdjudicatorsAdmin(admin.ModelAdmin):
    model = DrawsAdjudicators


class RoundsAdmin(admin.ModelAdmin):
    model = Rounds
    list_display = ["name"]
    search_fields = ["name"]


class SpeakerResultsAdmin(admin.ModelAdmin):
    model = SpeakerResults


class SpeakersAdmin(admin.ModelAdmin):
    model = Speakers
    list_display = ["name", "nickname"]
    search_fields = ["name", "nickname"]


class TeamResultsAdmin(admin.ModelAdmin):
    model = TeamResults


class TeamsAdmin(admin.ModelAdmin):
    model = Teams
    list_display = ["name"]
    search_fields = ["name"]


admin.site.register(Adjudicators, AdjudicatorsAdmin)
admin.site.register(Draws, DrawsAdmin)
admin.site.register(DrawsAdjudicators, DrawsAdjudicatorsAdmin)
admin.site.register(Rounds, RoundsAdmin)
admin.site.register(SpeakerResults, SpeakerResultsAdmin)
admin.site.register(Speakers, SpeakersAdmin)
admin.site.register(TeamResults, TeamResultsAdmin)
admin.site.register(Teams, TeamsAdmin)
