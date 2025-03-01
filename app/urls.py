from rest_framework import routers

from .views import (
    TournamentsViewSet,
)

app_router = routers.SimpleRouter()
app_router.register(r"app/tournaments", TournamentsViewSet)
