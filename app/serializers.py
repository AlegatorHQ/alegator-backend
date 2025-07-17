from rest_framework import serializers

from .models import Tournaments, Usertournament


class TournamentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournaments
        fields = [
            "id",
            "name",
            "description_tournament",
            "tournament_status",
            "avoid_same_institution",
            "shortname",
            "place",
            "missing_feedbacks",
            "feedback_description",
            "minimum_panel_score",
            "check_in",
            "start_date",
            "end_date",
            "creator",
        ]


class UsertournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usertournament
        fields = ["id", "user", "tournament", "role"]
