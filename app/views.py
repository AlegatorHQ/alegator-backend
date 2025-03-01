from rest_framework import viewsets

from . import permissions
from .models import Tournaments
from .serializers import TournamentsSerializer


class TournamentsViewSet(viewsets.ModelViewSet):
    queryset = Tournaments.objects.all()
    serializer_class = TournamentsSerializer
    permission_classes = (permissions.TournamentsPermission,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
