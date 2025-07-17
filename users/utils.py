import os
from supabase import create_client
from django.core.exceptions import ImproperlyConfigured

def get_supabase_client():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    if not url or not key:
        raise ImproperlyConfigured(
            "SUPABASE_URL and SUPABASE_KEY must be set in environment variables."
        )
    return create_client(url, key)

def validate_supabase_token(jwt_token):
    supabase = get_supabase_client()
    try:
        user = supabase.auth.get_user(jwt_token)
        return user
    except Exception:
        return None
