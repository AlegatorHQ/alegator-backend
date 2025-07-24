from rest_framework import serializers
from django.contrib.auth import get_user_model
from app.models import Usertournament, Tournaments

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'province']


class TournamentForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournaments
        fields = ['id', 'name', 'tournament_status']

class UserTournamentSerializer(serializers.ModelSerializer):
    tournament = TournamentForUserSerializer(read_only=True)
    class Meta:
        model = Usertournament
        fields = ['role', 'tournament'] 