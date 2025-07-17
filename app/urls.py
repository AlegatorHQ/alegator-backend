from rest_framework import routers

from .views import (
    TournamentsViewSet,
    UsertournamentViewSet,
    UserViewSet,
)

app_router = routers.SimpleRouter()
app_router.register(r"tournaments", TournamentsViewSet)
app_router.register(r"usertournament", UsertournamentViewSet)
app_router.register(r"users", UserViewSet)
