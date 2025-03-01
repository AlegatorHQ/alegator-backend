from rest_framework import serializers

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


class AdjudicatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adjudicators
        fields = [
            "id",
            "name",
            "province",
            "institution",
            "team_representation",
            "score",
        ]


class DrawsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Draws
        fields = ["id", "round", "speaker_position", "adjudicator", "draw_status"]


class DrawsAdjudicatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrawsAdjudicators
        fields = ["id", "adjudicator", "role"]


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


class SpeakerResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakerResults
        fields = ["id", "draw", "speaker", "speaker_points"]


class SpeakersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speakers
        fields = [
            "id",
            "name",
            "province",
            "nickname",
            "status",
            "institution",
            "is_novice",
        ]


class TeamResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamResults
        fields = ["id", "draw", "team", "position", "points"]


class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ["id", "name", "speaker_1", "speaker_2"]
