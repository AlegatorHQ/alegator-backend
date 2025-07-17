from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from . import permissions
from .models import User
from .serializers import UserSerializer
from .utils import validate_supabase_token


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.UserPermission,)


class SupabaseLoginView(APIView):
    """
    Custom login view to authenticate users with a Supabase JWT.
    """
    def post(self, request, *args, **kwargs):
        supabase_token = request.data.get('access_token')
        if not supabase_token:
            return Response(
                {'error': 'Supabase access token not provided.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        supabase_user = validate_supabase_token(supabase_token)
        if not supabase_user:
            return Response(
                {'error': 'Invalid or expired Supabase token.'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        try:
            # The object returned by supabase-py's get_user has the user data under a `user` attribute
            user_email = supabase_user.user.email
            # A unique username is required by default in Django's User model.
            # We can use the email's prefix or the full email if it's unique.
            username = user_email
        except (AttributeError, KeyError):
            return Response(
                {'error': 'Could not retrieve user details from Supabase token.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Get or create the user in the Django database
        user, created = User.objects.get_or_create(
            email=user_email,
            defaults={'username': username} # Make sure your custom User model can handle this
        )

        if created:
            # You might want to populate other user fields here
            # e.g., user.first_name = ...
            user.save()

        # Generate a JWT for the Django user
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        })