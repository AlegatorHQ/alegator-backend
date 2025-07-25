from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model # Import get_user_model

from .models import Tournaments, Usertournament
from .serializers import TournamentsSerializer
from sgtd.models import Speakers, Judges, Teams # Import models
from sgtd.serializers import SpeakersSerializer, JudgesSerializer, TeamsSerializer # Import serializers
from users.serializers import UserTournamentSerializer # Import UserTournamentSerializer

User = get_user_model()

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

    @action(detail=True, methods=['get', 'post'], url_path='speakers', permission_classes=[IsAuthenticated])
    def speakers(self, request, pk=None):
        tournament = self.get_object()
        if request.method == 'GET':
            speakers = Speakers.objects.filter(tournament=tournament)
            serializer = SpeakersSerializer(speakers, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = SpeakersSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(tournament=tournament)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get', 'post'], url_path='judges', permission_classes=[IsAuthenticated])
    def judges(self, request, pk=None):
        tournament = self.get_object()
        if request.method == 'GET':
            judges = Judges.objects.filter(tournament=tournament)
            serializer = JudgesSerializer(judges, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = JudgesSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(tournament=tournament)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get', 'post'], url_path='teams', permission_classes=[IsAuthenticated])
    def teams(self, request, pk=None):
        tournament = self.get_object()
        if request.method == 'GET':
            teams = Teams.objects.filter(tournament=tournament)
            serializer = TeamsSerializer(teams, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = TeamsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(tournament=tournament)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], url_path='register', permission_classes=[IsAuthenticated])
    def register(self, request, pk=None):
        tournament = self.get_object()
        user_id = request.data.get('user_id')
        role = request.data.get('role')

        if not role:
            return Response({"detail": "Role is required."}, status=status.HTTP_400_BAD_REQUEST)

        if user_id:
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            user = request.user # Use authenticated user if no user_id is provided

        # Check if user is already registered for this tournament with this role
        if Usertournament.objects.filter(user=user, tournament=tournament, role=role).exists():
            return Response({"detail": f"User is already registered as {role} for this tournament."}, status=status.HTTP_409_CONFLICT) # 409 Conflict

        usertournament = Usertournament.objects.create(
            user=user, tournament=tournament, role=role
        )
        serializer = UserTournamentSerializer(usertournament)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
