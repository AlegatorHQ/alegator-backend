from django.contrib import admin

from .models import (
    Checkins,
    Draws,
    Drawsjudges,
    Feedbacks,
    Judges,
    Rounds,
    Speakerresults,
    Speakers,
    Teamresults,
    Teams,
)


class CheckinsAdmin(admin.ModelAdmin):
    model = Checkins


class DrawsAdmin(admin.ModelAdmin):
    model = Draws


class DrawsjudgesAdmin(admin.ModelAdmin):
    model = Drawsjudges


class FeedbacksAdmin(admin.ModelAdmin):
    model = Feedbacks


class JudgesAdmin(admin.ModelAdmin):
    model = Judges
    list_display = ["user"]
    search_fields = ["user__first_name", "user__last_name"]


class RoundsAdmin(admin.ModelAdmin):
    model = Rounds
    list_display = ["name"]
    search_fields = ["name"]


class SpeakerresultsAdmin(admin.ModelAdmin):
    model = Speakerresults


class SpeakersAdmin(admin.ModelAdmin):
    model = Speakers
    list_display = ["user"]
    search_fields = ["user__first_name", "user__last_name"]


class TeamresultsAdmin(admin.ModelAdmin):
    model = Teamresults


class TeamsAdmin(admin.ModelAdmin):
    model = Teams
    list_display = ["name"]
    search_fields = ["name"]


admin.site.register(Checkins, CheckinsAdmin)
admin.site.register(Draws, DrawsAdmin)
admin.site.register(Drawsjudges, DrawsjudgesAdmin)
admin.site.register(Feedbacks, FeedbacksAdmin)
admin.site.register(Judges, JudgesAdmin)
admin.site.register(Rounds, RoundsAdmin)
admin.site.register(Speakerresults, SpeakerresultsAdmin)
admin.site.register(Speakers, SpeakersAdmin)
admin.site.register(Teamresults, TeamresultsAdmin)
admin.site.register(Teams, TeamsAdmin)
