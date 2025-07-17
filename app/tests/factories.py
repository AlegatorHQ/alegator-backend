from datetime import timezone
import factory
from factory.django import DjangoModelFactory

from ..models import Tournaments, Usertournament, Users

class UserFactory(DjangoModelFactory):
    class Meta:
        model = Users
        django_get_or_create = ("email",)

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    province = factory.Faker("province")
    is_staff = False
    is_superuser = False
    is_active = True

    @staticmethod
    def with_password(password, **kwargs):
        user = UserFactory.build(**kwargs)
        user.set_password(password)
        user.save()
        return user


class AdminUserFactory(UserFactory):
    username = factory.Faker("user_name")
    email = factory.Faker("email")
    is_staff = True
    is_superuser = True
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")

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
    creator = factory.SubFactory("app.tests.factories.UserFactory")
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
