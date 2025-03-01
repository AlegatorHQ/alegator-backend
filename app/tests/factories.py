from datetime import timezone
from django.contrib.auth import get_user_model
import factory
from factory.django import DjangoModelFactory

from ..models import Tournaments

User = get_user_model()


class TournamentsFactory(DjangoModelFactory):
    class Meta:
        model = Tournaments

    name = factory.Faker("text")
    tournament_status = factory.Faker("text")
    avoid_same_institution = factory.Faker("boolean")
    missing_feedbacks = factory.Faker("boolean")
    minimum_panel_score = factory.Faker("random_int")
    check_in = factory.Faker("boolean")
    start_date = factory.Faker("date_object")
    end_date = factory.Faker("date_object")
    creator = factory.SubFactory("users.tests.factories.UserFactory")
    created_at = factory.Faker("date_time", tzinfo=timezone.utc)
    updated_at = factory.Faker("date_time", tzinfo=timezone.utc)
