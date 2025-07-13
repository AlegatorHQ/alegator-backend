from datetime import timezone
from django.contrib.auth import get_user_model
import factory
from factory.django import DjangoModelFactory

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

User = get_user_model()


class SpeakersFactory(DjangoModelFactory):
    class Meta:
        model = Speakers

    name = factory.Faker("text")
    province = factory.Faker("text")
    delegation = factory.Faker("text")


class TeamsFactory(DjangoModelFactory):
    class Meta:
        model = Teams

    name = factory.Faker("text")
    speaker_1 = factory.SubFactory("users.tests.factories.UserFactory")
    speaker_2 = factory.SubFactory("users.tests.factories.UserFactory")
    teamtype = factory.Faker("text")


class JudgesFactory(DjangoModelFactory):
    class Meta:
        model = Judges

    name = factory.Faker("text")
    province = factory.Faker("text")
    delegation = factory.Faker("text")
    team = factory.SubFactory("sgtd.tests.factories.TeamsFactory")
    basescore = factory.Faker(
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
    ag = factory.SubFactory("sgtd.tests.factories.SpeakersFactory")
    draw_status = factory.Faker("text")
    ao = factory.SubFactory("sgtd.tests.factories.SpeakersFactory")
    bg = factory.SubFactory("sgtd.tests.factories.SpeakersFactory")
    bo = factory.SubFactory("sgtd.tests.factories.SpeakersFactory")


class DrawsjudgesFactory(DjangoModelFactory):
    class Meta:
        model = Drawsjudges

    draw = factory.SubFactory("sgtd.tests.factories.JudgesFactory")
    judge = factory.SubFactory("sgtd.tests.factories.JudgesFactory")
    role = factory.Faker("text")


class TeamresultsFactory(DjangoModelFactory):
    class Meta:
        model = Teamresults

    draw = factory.SubFactory("sgtd.tests.factories.DrawsFactory")
    team = factory.SubFactory("sgtd.tests.factories.TeamsFactory")
    position = factory.Faker("text")
    points = factory.Faker("random_int")


class SpeakerresultsFactory(DjangoModelFactory):
    class Meta:
        model = Speakerresults

    draw = factory.SubFactory("sgtd.tests.factories.DrawsFactory")
    speaker = factory.SubFactory("sgtd.tests.factories.SpeakersFactory")
    speaker_points = factory.Faker(
        "pydecimal", left_digits=1, right_digits=2, min_value=None, max_value=None
    )
    team_result = factory.SubFactory("sgtd.tests.factories.TeamresultsFactory")


class CheckinsFactory(DjangoModelFactory):
    class Meta:
        model = Checkins

    update_at = factory.Faker("date_time", tzinfo=timezone.utc)
    round = factory.SubFactory("sgtd.tests.factories.RoundsFactory")
    speaker = factory.SubFactory("sgtd.tests.factories.SpeakersFactory")


class FeedbacksFactory(DjangoModelFactory):
    class Meta:
        model = Feedbacks

    draw = factory.SubFactory("sgtd.tests.factories.DrawsFactory")
    given_by = factory.Faker("text")
    target = factory.Faker("text")
    comment = factory.Faker("text")
    score = factory.Faker("random_int")
