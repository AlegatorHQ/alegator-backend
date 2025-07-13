from datetime import timezone
from django.contrib.auth import get_user_model
import factory
from factory.django import DjangoModelFactory

from ..models import Tournaments, Usertournament

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


class UsertournamentFactory(DjangoModelFactory):
    class Meta:
        model = Usertournament

    role = factory.Faker("text")

    @factory.post_generation
    def user(self, create, extracted, **kwargs):
        if not create:
            return
        # if related model instances are provided, add them to the relation
        if extracted:
            for model in extracted:
                self.user.add(model)
        # by default the relation is empty

    @factory.post_generation
    def tournament(self, create, extracted, **kwargs):
        if not create:
            return
        # if related model instances are provided, add them to the relation
        if extracted:
            for model in extracted:
                self.tournament.add(model)
        # by default the relation is empty
