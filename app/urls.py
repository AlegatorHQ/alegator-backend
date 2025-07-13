from rest_framework import routers

from .views import (
    TournamentsViewSet,
    UsertournamentViewSet,
)

app_router = routers.SimpleRouter()
app_router.register(r"app/tournaments", TournamentsViewSet)
app_router.register(r"app/usertournament", UsertournamentViewSet)
