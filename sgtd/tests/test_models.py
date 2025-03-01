from django.test import TestCase

from ..models import (
    Adjudicators,
    Draws,
    DrawsAdjudicators,
    Rounds,
    SpeakerResults,
    Speakers,
    TeamResults,
    Teams,
)
from .factories import (
    SpeakersFactory,
    TeamsFactory,
    AdjudicatorsFactory,
    RoundsFactory,
    DrawsFactory,
    DrawsAdjudicatorsFactory,
    TeamResultsFactory,
    SpeakerResultsFactory,
)


class SpeakersTestCase(TestCase):
    def test_create_speakers(self):
        """Test that Speakers can be created using its factory."""

        obj = SpeakersFactory()
        assert Speakers.objects.all().get() == obj


class TeamsTestCase(TestCase):
    def test_create_teams(self):
        """Test that Teams can be created using its factory."""

        obj = TeamsFactory()
        assert Teams.objects.all().get() == obj


class AdjudicatorsTestCase(TestCase):
    def test_create_adjudicators(self):
        """Test that Adjudicators can be created using its factory."""

        obj = AdjudicatorsFactory()
        assert Adjudicators.objects.all().get() == obj


class RoundsTestCase(TestCase):
    def test_create_rounds(self):
        """Test that Rounds can be created using its factory."""

        obj = RoundsFactory()
        assert Rounds.objects.all().get() == obj


class DrawsTestCase(TestCase):
    def test_create_draws(self):
        """Test that Draws can be created using its factory."""

        obj = DrawsFactory()
        assert Draws.objects.all().get() == obj


class DrawsAdjudicatorsTestCase(TestCase):
    def test_create_draws_adjudicators(self):
        """Test that DrawsAdjudicators can be created using its factory."""

        obj = DrawsAdjudicatorsFactory()
        assert DrawsAdjudicators.objects.all().get() == obj


class TeamResultsTestCase(TestCase):
    def test_create_team_results(self):
        """Test that TeamResults can be created using its factory."""

        obj = TeamResultsFactory()
        assert TeamResults.objects.all().get() == obj


class SpeakerResultsTestCase(TestCase):
    def test_create_speaker_results(self):
        """Test that SpeakerResults can be created using its factory."""

        obj = SpeakerResultsFactory()
        assert SpeakerResults.objects.all().get() == obj
