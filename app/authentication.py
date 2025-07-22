import jwt
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()

class SupabaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return None

        try:
            prefix, token = auth_header.split(' ')
            if prefix != 'Bearer':
                raise AuthenticationFailed('Invalid token prefix')
        except (ValueError, TypeError):
            raise AuthenticationFailed('Invalid Authorization header format')

        if not token:
            return None

        try:
            payload = jwt.decode(
                token, 
                settings.SUPABASE_JWT_SECRET, 
                algorithms=['HS256']
            )
            
            supabase_id = payload.get('sub')
            if not supabase_id:
                raise AuthenticationFailed('Token does not contain user ID')

            user, created = User.objects.get_or_create(
                supabase_id=supabase_id,
                defaults={
                    'username': payload.get('email', supabase_id),
                    'email': payload.get('email', ''),
    
                }
            )

            return (user, token)

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')
        except Exception as e:
            raise AuthenticationFailed('Could not authenticate user') 