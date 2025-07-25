from rest_framework import serializers

from .models import Tournaments, Usertournament


class TournamentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournaments
        fields = [
            "id",
            "tournament_status",
            "avoid_same_institution",
            "shortname",
            "place",
            "missing_feedbacks",
            "speaker_criteria",
            "minimum_panel_score",
            "check_in",
            "start_date",
            "end_date",
            "team_criteria",
            "creator",
            "updated_at",
        ]


class UsertournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usertournament
        fields = ["id", "user", "tournament", "role"]
