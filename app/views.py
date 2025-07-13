from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from . import permissions
from .models import Tournaments, Usertournament
from .serializers import TournamentsSerializer, UsertournamentSerializer


class TournamentsViewSet(viewsets.ModelViewSet):
    queryset = Tournaments.objects.all()
    serializer_class = TournamentsSerializer
    permission_classes = (permissions.TournamentsPermission,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class UsertournamentViewSet(viewsets.ModelViewSet):
    queryset = Usertournament.objects.all()
    serializer_class = UsertournamentSerializer
    permission_classes = (permissions.UsertournamentPermission,)
    filter_backend = [DjangoFilterBackend]
    filterset_fields = {
        "role": ["icontains"],
    }
