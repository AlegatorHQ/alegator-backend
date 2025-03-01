from django.test import TestCase

from ..models import Tournaments
from .factories import TournamentsFactory


class TournamentsTestCase(TestCase):
    def test_create_tournaments(self):
        """Test that Tournaments can be created using its factory."""

        obj = TournamentsFactory()
        assert Tournaments.objects.all().get() == obj
