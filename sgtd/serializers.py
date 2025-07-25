from rest_framework import serializers

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


class CheckinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkins
        fields = ["id", "created_at", "update_at", "round", "speaker"]


class DrawsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Draws
        fields = ["id", "round", "ag", "draw_status", "bo"]


class DrawsjudgesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drawsjudges
        fields = ["judge", "role", "is_checked"]


class FeedbacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedbacks
        fields = ["id", "draw", "target", "comment", "score", "status"]


class JudgesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judges
        fields = ["id", "name", "province", "delegation", "team", "basescore"]


class RoundsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rounds
        fields = [
            "id",
            "name",
            "motion",
            "infoslide",
            "round_number",
            "round_status",
            "round_type",
            "is_silenced",
        ]


class SpeakerresultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speakerresults
        fields = ["id", "draw", "speaker", "speaker_points", "is_iron", "team_result"]


class SpeakersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speakers
        fields = ["id", "user", "province", "delegation", "is_novice"]


class TeamresultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teamresults
        fields = ["id", "draw", "team", "position", "points"]


class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ["id", "name", "speaker_1", "speaker_2"]