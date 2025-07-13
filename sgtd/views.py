from rest_framework import viewsets

from . import permissions
from .models import (
    Checkins,
    Draws,
    Feedbacks,
    Judges,
    Rounds,
    Speakerresults,
    Speakers,
    Teamresults,
    Teams,
)
from .serializers import (
    CheckinsSerializer,
    DrawsSerializer,
    FeedbacksSerializer,
    JudgesSerializer,
    RoundsSerializer,
    SpeakerresultsSerializer,
    SpeakersSerializer,
    TeamresultsSerializer,
    TeamsSerializer,
)


class CheckinsViewSet(viewsets.ModelViewSet):
    queryset = Checkins.objects.all()
    serializer_class = CheckinsSerializer
    permission_classes = (permissions.CheckinsPermission,)


class DrawsViewSet(viewsets.ModelViewSet):
    queryset = Draws.objects.all()
    serializer_class = DrawsSerializer
    permission_classes = (permissions.DrawsPermission,)


class FeedbacksViewSet(viewsets.ModelViewSet):
    queryset = Feedbacks.objects.all()
    serializer_class = FeedbacksSerializer
    permission_classes = (permissions.FeedbacksPermission,)


class JudgesViewSet(viewsets.ModelViewSet):
    queryset = Judges.objects.all()
    serializer_class = JudgesSerializer
    permission_classes = (permissions.JudgesPermission,)


class RoundsViewSet(viewsets.ModelViewSet):
    queryset = Rounds.objects.all()
    serializer_class = RoundsSerializer
    permission_classes = (permissions.RoundsPermission,)


class SpeakerresultsViewSet(viewsets.ModelViewSet):
    queryset = Speakerresults.objects.all()
    serializer_class = SpeakerresultsSerializer
    permission_classes = (permissions.SpeakerresultsPermission,)


class SpeakersViewSet(viewsets.ModelViewSet):
    queryset = Speakers.objects.all()
    serializer_class = SpeakersSerializer
    permission_classes = (permissions.SpeakersPermission,)


class TeamresultsViewSet(viewsets.ModelViewSet):
    queryset = Teamresults.objects.all()
    serializer_class = TeamresultsSerializer
    permission_classes = (permissions.TeamresultsPermission,)


class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer
    permission_classes = (permissions.TeamsPermission,)
