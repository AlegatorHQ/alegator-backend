from rest_framework import routers

from .views import (
    CheckinsViewSet,
    DrawsViewSet,
    FeedbacksViewSet,
    JudgesViewSet,
    RoundsViewSet,
    SpeakerresultsViewSet,
    SpeakersViewSet,
    TeamresultsViewSet,
    TeamsViewSet,
)

sgtd_router = routers.SimpleRouter()
sgtd_router.register(r"sgtd/checkins", CheckinsViewSet)
sgtd_router.register(r"sgtd/draws", DrawsViewSet)
sgtd_router.register(r"sgtd/feedbacks", FeedbacksViewSet)
sgtd_router.register(r"sgtd/judges", JudgesViewSet)
sgtd_router.register(r"sgtd/rounds", RoundsViewSet)
sgtd_router.register(r"sgtd/speakerresults", SpeakerresultsViewSet)
sgtd_router.register(r"sgtd/speakers", SpeakersViewSet)
sgtd_router.register(r"sgtd/teamresults", TeamresultsViewSet)
sgtd_router.register(r"sgtd/teams", TeamsViewSet)
