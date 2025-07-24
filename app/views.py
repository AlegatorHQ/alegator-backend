from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Tournaments, Usertournament
from .serializers import TournamentsSerializer


class TournamentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tournaments to be viewed or edited.
    """
    queryset = Tournaments.objects.all()
    serializer_class = TournamentsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        tournament = serializer.save(creator=self.request.user)
        Usertournament.objects.create(
            user=self.request.user, tournament=tournament, role="admin"
        )
