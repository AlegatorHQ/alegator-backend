from django.test import TestCase

from ..models import (
    Checkins,
    Draws,
    Drawsjudges,
    Feedbacks,
    Judges,
    Rounds,
    Speakerresults,
    Speakers,
    Teamresults,
    Teams,
)
from .factories import (
    SpeakersFactory,
    TeamsFactory,
    JudgesFactory,
    RoundsFactory,
    DrawsFactory,
    DrawsjudgesFactory,
    TeamresultsFactory,
    SpeakerresultsFactory,
    CheckinsFactory,
    FeedbacksFactory,
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


class JudgesTestCase(TestCase):
    def test_create_judges(self):
        """Test that Judges can be created using its factory."""

        obj = JudgesFactory()
        assert Judges.objects.all().get() == obj


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


class DrawsjudgesTestCase(TestCase):
    def test_create_drawsjudges(self):
        """Test that Drawsjudges can be created using its factory."""

        obj = DrawsjudgesFactory()
        assert Drawsjudges.objects.all().get() == obj


class TeamresultsTestCase(TestCase):
    def test_create_teamresults(self):
        """Test that Teamresults can be created using its factory."""

        obj = TeamresultsFactory()
        assert Teamresults.objects.all().get() == obj


class SpeakerresultsTestCase(TestCase):
    def test_create_speakerresults(self):
        """Test that Speakerresults can be created using its factory."""

        obj = SpeakerresultsFactory()
        assert Speakerresults.objects.all().get() == obj


class CheckinsTestCase(TestCase):
    def test_create_checkins(self):
        """Test that Checkins can be created using its factory."""

        obj = CheckinsFactory()
        assert Checkins.objects.all().get() == obj


class FeedbacksTestCase(TestCase):
    def test_create_feedbacks(self):
        """Test that Feedbacks can be created using its factory."""

        obj = FeedbacksFactory()
        assert Feedbacks.objects.all().get() == obj
