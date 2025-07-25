from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserTournamentSerializer
from app.models import Usertournament
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404 # Importar get_object_or_404

User = get_user_model()

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='by-email', permission_classes=[IsAuthenticated])
    def by_email(self, request):
        """
        Permite buscar un usuario por su dirección de correo electrónico.
        Requiere autenticación.
        Ejemplo de uso: GET /api/v1/users/by-email?email=usuario@example.com
        """
        email = request.query_params.get('email', None)
        
        if email is None:
            return Response({"detail": "Email parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=email)
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"detail": "User with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'], url_path='me/tournaments', permission_classes=[IsAuthenticated])
    def my_tournaments(self, request):
        """
        Lists the tournaments the authenticated user is participating in or organizing.
        """
        user = request.user
        user_tournaments = Usertournament.objects.filter(user=user)
        serializer = UserTournamentSerializer(user_tournaments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get', 'patch'], url_path='me', permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        elif request.method == 'PATCH':
            serializer = self.get_serializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)