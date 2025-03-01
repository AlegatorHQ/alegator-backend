from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from . import permissions
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
from .serializers import (
    AdjudicatorsSerializer,
    DrawsSerializer,
    DrawsAdjudicatorsSerializer,
    RoundsSerializer,
    SpeakerResultsSerializer,
    SpeakersSerializer,
    TeamResultsSerializer,
    TeamsSerializer,
)


class AdjudicatorsViewSet(viewsets.ModelViewSet):
    queryset = Adjudicators.objects.all()
    serializer_class = AdjudicatorsSerializer
    permission_classes = (permissions.AdjudicatorsPermission,)
    filter_backend = [DjangoFilterBackend]
    filterset_fields = {
        "name": ["icontains"],
    }


class DrawsViewSet(viewsets.ModelViewSet):
    queryset = Draws.objects.all()
    serializer_class = DrawsSerializer
    permission_classes = (permissions.DrawsPermission,)


class DrawsAdjudicatorsViewSet(viewsets.ModelViewSet):
    queryset = DrawsAdjudicators.objects.all()
    serializer_class = DrawsAdjudicatorsSerializer
    permission_classes = (permissions.DrawsAdjudicatorsPermission,)


class RoundsViewSet(viewsets.ModelViewSet):
    queryset = Rounds.objects.all()
    serializer_class = RoundsSerializer
    permission_classes = (permissions.RoundsPermission,)


class SpeakerResultsViewSet(viewsets.ModelViewSet):
    queryset = SpeakerResults.objects.all()
    serializer_class = SpeakerResultsSerializer
    permission_classes = (permissions.SpeakerResultsPermission,)


class SpeakersViewSet(viewsets.ModelViewSet):
    queryset = Speakers.objects.all()
    serializer_class = SpeakersSerializer
    permission_classes = (permissions.SpeakersPermission,)


class TeamResultsViewSet(viewsets.ModelViewSet):
    queryset = TeamResults.objects.all()
    serializer_class = TeamResultsSerializer
    permission_classes = (permissions.TeamResultsPermission,)


class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer
    permission_classes = (permissions.TeamsPermission,)
    filter_backend = [DjangoFilterBackend]
    filterset_fields = {
        "name": ["icontains"],
    }
