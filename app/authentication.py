import jwt
import logging
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()
logger = logging.getLogger(__name__)

class SupabaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        print(f"DEBUG: Incoming headers: {request.headers}")
        if not auth_header:
            print("DEBUG: No Authorization header found.")
            return None

        print(f"DEBUG: Authorization header found: {auth_header}")
        try:
            prefix, token = auth_header.split(' ')
            if prefix.lower() != 'bearer':
                print(f"DEBUG: Invalid token prefix: {prefix}")
                return None
        except (ValueError, TypeError):
            print("DEBUG: Invalid Authorization header format.")
            raise AuthenticationFailed('Invalid Authorization header format')

        if not token:
            print("DEBUG: Token is empty after split.")
            return None

        try:
            print("DEBUG: Attempting to decode token...")
            payload = jwt.decode(
                token,
                settings.SUPABASE_JWT_SECRET,
                algorithms=['HS256'],
                audience='authenticated'
            )
            print(f"DEBUG: Token decoded successfully. Payload: {payload}")
            supabase_id = payload.get('sub')
            if not supabase_id:
                print("DEBUG: Token does not contain 'sub' (user ID).")
                raise AuthenticationFailed('Token does not contain user ID')

            user, created = User.objects.get_or_create(
                supabase_id=supabase_id,
                defaults={'username': payload.get('email', supabase_id), 'email': payload.get('email', '')}
            )
            if created:
                print(f"DEBUG: Created new user with supabase_id: {supabase_id}")
            else:
                print(f"DEBUG: Found existing user with supabase_id: {supabase_id}")

            return (user, token)
        except jwt.ExpiredSignatureError:
            print("DEBUG: Token has expired.")
            raise AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError as e:
            print(f"DEBUG: Invalid token. JWT Decode Error: {e}")
            print("DEBUG: THIS IS LIKELY DUE TO A MISMATCHED SUPABASE_JWT_SECRET.")
            raise AuthenticationFailed(f'Invalid token: {e}')
        except Exception as e:
            print(f"DEBUG: An unexpected error occurred during authentication: {e}")
            raise AuthenticationFailed('Could not authenticate user') 