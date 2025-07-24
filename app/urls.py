from rest_framework import routers
from .views import TournamentsViewSet

router = routers.DefaultRouter()

router.register(r'tournaments', TournamentsViewSet)
