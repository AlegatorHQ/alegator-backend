from rest_framework import routers

from .views import (
    CheckinsViewSet,
    DrawsViewSet,
    FeedbacksViewSet,
    # JudgesViewSet, # Removed
    RoundsViewSet,
    SpeakerresultsViewSet,
    # SpeakersViewSet, # Removed
    TeamresultsViewSet,
    # TeamsViewSet, # Removed
)

sgtd_router = routers.SimpleRouter()
sgtd_router.register(r"sgtd/checkins", CheckinsViewSet)
sgtd_router.register(r"sgtd/draws", DrawsViewSet)
sgtd_router.register(r"sgtd/feedbacks", FeedbacksViewSet)
# sgtd_router.register(r"sgtd/judges", JudgesViewSet) # Removed
sgtd_router.register(r"sgtd/rounds", RoundsViewSet)
sgtd_router.register(r"sgtd/speakerresults", SpeakerresultsViewSet)
# sgtd_router.register(r"sgtd/speakers", SpeakersViewSet) # Removed
sgtd_router.register(r"sgtd/teamresults", TeamresultsViewSet)
# sgtd_router.register(r"sgtd/teams", TeamsViewSet) # Removed