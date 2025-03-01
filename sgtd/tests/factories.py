from django.contrib.auth import get_user_model
import factory
from factory.django import DjangoModelFactory

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

User = get_user_model()


class SpeakersFactory(DjangoModelFactory):
    class Meta:
        model = Speakers

    name = factory.Faker("text")
    province = factory.Faker("text")
    nickname = factory.Faker("text")
    status = factory.Faker("boolean")
    institution = factory.Faker("text")


class TeamsFactory(DjangoModelFactory):
    class Meta:
        model = Teams

    name = factory.Faker("text")
    speaker_1 = factory.SubFactory("users.tests.factories.UserFactory")
    speaker_2 = factory.SubFactory("users.tests.factories.UserFactory")


class AdjudicatorsFactory(DjangoModelFactory):
    class Meta:
        model = Adjudicators

    name = factory.Faker("text")
    province = factory.Faker("text")
    institution = factory.Faker("text")
    team_representation = factory.SubFactory("sgtd.tests.factories.TeamsFactory")
    score = factory.Faker(
        "pydecimal", left_digits=1, right_digits=2, min_value=None, max_value=None
    )


class RoundsFactory(DjangoModelFactory):
    class Meta:
        model = Rounds

    name = factory.Faker("text")
    motion = factory.Faker("text")
    infoslide = factory.Faker("text")
    round_number = factory.Faker("random_int")
    round_status = factory.Faker("text")
    round_type = factory.Faker("boolean")
    is_silenced = factory.Faker("boolean")


class DrawsFactory(DjangoModelFactory):
    class Meta:
        model = Draws

    round = factory.SubFactory("sgtd.tests.factories.RoundsFactory")
    speaker_position = factory.SubFactory("sgtd.tests.factories.SpeakersFactory")
    adjudicator = factory.SubFactory("sgtd.tests.factories.AdjudicatorsFactory")
    draw_status = factory.Faker("text")


class DrawsAdjudicatorsFactory(DjangoModelFactory):
    class Meta:
        model = DrawsAdjudicators

    draw = factory.SubFactory("sgtd.tests.factories.AdjudicatorsFactory")
    adjudicator = factory.SubFactory("sgtd.tests.factories.AdjudicatorsFactory")
    role = factory.Faker("text")


class TeamResultsFactory(DjangoModelFactory):
    class Meta:
        model = TeamResults

    draw = factory.SubFactory("sgtd.tests.factories.DrawsFactory")
    team = factory.SubFactory("sgtd.tests.factories.TeamsFactory")
    position = factory.Faker("text")
    points = factory.Faker("random_int")


class SpeakerResultsFactory(DjangoModelFactory):
    class Meta:
        model = SpeakerResults

    draw = factory.SubFactory("sgtd.tests.factories.DrawsFactory")
    speaker = factory.SubFactory("sgtd.tests.factories.SpeakersFactory")
    speaker_points = factory.Faker(
        "pydecimal", left_digits=1, right_digits=2, min_value=None, max_value=None
    )
