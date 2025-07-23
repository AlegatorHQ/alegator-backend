from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import response, status, viewsets
from rest_framework import permissions as drf_permissions
from rest_framework.decorators import action

from . import permissions
from .models import Tournaments, Usertournament
from .serializers import TournamentsSerializer, UsertournamentSerializer
from sgtd.models import Judges, Speakers
from sgtd.serializers import JudgesSerializer, SpeakersSerializer


class TournamentsViewSet(viewsets.ModelViewSet):
    queryset = Tournaments.objects.all()
    serializer_class = TournamentsSerializer
    permission_classes = (permissions.TournamentsPermission,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    @action(
        detail=True,
        methods=["post"],
        permission_classes=[drf_permissions.IsAuthenticated],
    )
    def register(self, request, pk=None):
        tournament = self.get_object()
        role = request.data.get("role", "participant")
        usertournament, created = Usertournament.objects.get_or_create(
            user=request.user,
            tournament=tournament,
            defaults={"role": role},
        )
        if not created and usertournament.role != role:
            usertournament.role = role
            usertournament.save()

        serializer = UsertournamentSerializer(usertournament)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["get"])
    def participants(self, request, pk=None):
        tournament = self.get_object()
        speakers = Speakers.objects.filter(tournament=tournament)
        judges = Judges.objects.filter(tournament=tournament)
        speakers_serializer = SpeakersSerializer(speakers, many=True)
        judges_serializer = JudgesSerializer(judges, many=True)
        return response.Response(
            {
                "speakers": speakers_serializer.data,
                "judges": judges_serializer.data,
            }
        )

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[drf_permissions.IsAuthenticated],
    )
    def my_data(self, request, pk=None):
        tournament = self.get_object()
        try:
            user_tournament = Usertournament.objects.get(
                user=request.user, tournament=tournament
            )
            role = user_tournament.role
        except Usertournament.DoesNotExist:
            return response.Response(
                {"detail": "User not registered in this tournament."},
                status=status.HTTP_404_NOT_FOUND,
            )

        speaker_profile = None
        judge_profile = None

        if role == "participant" or role == "speaker":
            try:
                # This logic assumes user's full name matches speaker's name. This might be fragile.
                speaker = Speakers.objects.get(
                    tournament=tournament, name__iexact=request.user.get_full_name()
                )
                speaker_profile = SpeakersSerializer(speaker).data
            except Speakers.DoesNotExist:
                pass  # Or handle as an error

        if role == "judge":
            try:
                # This logic assumes user's full name matches judge's name. This might be fragile.
                judge = Judges.objects.get(
                    tournament=tournament, name__iexact=request.user.get_full_name()
                )
                judge_profile = JudgesSerializer(judge).data
            except Judges.DoesNotExist:
                pass  # Or handle as an error

        return response.Response(
            {
                "user_id": request.user.id,
                "tournament_id": tournament.id,
                "role": role,
                "speaker_profile": speaker_profile,
                "judge_profile": judge_profile,
            }
        )


class UsertournamentViewSet(viewsets.ModelViewSet):
    queryset = Usertournament.objects.all()
    serializer_class = UsertournamentSerializer
    permission_classes = (permissions.UsertournamentPermission,)
    filter_backend = [DjangoFilterBackend]
    filterset_fields = {
        "role": ["icontains"],
    }
