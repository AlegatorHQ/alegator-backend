from rest_framework import serializers
from .models import Tournaments, Usertournament


class TournamentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournaments
        fields = '__all__'
        read_only_fields = ('creator',)
        extra_kwargs = {
            'minimum_panel_score': {'default': 3}
        }


class UsertournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usertournament
        fields = '__all__'
