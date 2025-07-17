from django.test import TestCase

from ..models import Tournaments, Usertournament, Users
from .factories import TournamentsFactory, UsertournamentFactory, UserFactory

class UsersTestCase(TestCase):
    def test_create_users(self):
        """Test that Users can be created using its factory."""

        obj = UserFactory()
        assert Users.objects.all().get() == obj


class TournamentsTestCase(TestCase):
    def test_create_tournaments(self):
        """Test that Tournaments can be created using its factory."""

        obj = TournamentsFactory()
        assert Tournaments.objects.all().get() == obj


class UsertournamentTestCase(TestCase):
    def test_create_usertournament(self):
        """Test that Usertournament can be created using its factory."""

        obj = UsertournamentFactory()
        assert Usertournament.objects.all().get() == obj
