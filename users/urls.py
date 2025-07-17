from django.urls import path
from .views import SupabaseLoginView, UserViewSet
from rest_framework import routers

users_router = routers.SimpleRouter()
users_router.register(r"users/user", UserViewSet)

urlpatterns = [
    path('auth/login/', SupabaseLoginView.as_view(), name='supabase_login'),
]

urlpatterns += users_router.urls
