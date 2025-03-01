from rest_framework import routers

from .views import (
    AdjudicatorsViewSet,
    DrawsViewSet,
    DrawsAdjudicatorsViewSet,
    RoundsViewSet,
    SpeakerResultsViewSet,
    SpeakersViewSet,
    TeamResultsViewSet,
    TeamsViewSet,
)

sgtd_router = routers.SimpleRouter()
sgtd_router.register(r"sgtd/adjudicators", AdjudicatorsViewSet)
sgtd_router.register(r"sgtd/draws", DrawsViewSet)
sgtd_router.register(r"sgtd/draws-adjudicators", DrawsAdjudicatorsViewSet)
sgtd_router.register(r"sgtd/rounds", RoundsViewSet)
sgtd_router.register(r"sgtd/speaker-results", SpeakerResultsViewSet)
sgtd_router.register(r"sgtd/speakers", SpeakersViewSet)
sgtd_router.register(r"sgtd/team-results", TeamResultsViewSet)
sgtd_router.register(r"sgtd/teams", TeamsViewSet)
