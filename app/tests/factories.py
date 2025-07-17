from datetime import timezone
import factory
from factory import fuzzy
from factory.declarations import SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

from ..models import Tournaments, Usertournament, Users


class UserFactory(DjangoModelFactory):
    class Meta:
        model = Users
        django_get_or_create = ("email",)

    username = Faker("user_name")
    email = Faker("email")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    province = fuzzy.FuzzyChoice(
        ["Panamá", "Colón", "Chiriquí", "Bocas del Toro", "Herrera", "Los Santos", "Veraguas", "Coclé", "Darién"]
    )
    is_staff = False
    is_superuser = False
    is_authenticated = True
    is_active = True

    @staticmethod
    def with_password(password, **kwargs):
        user = UserFactory.build(**kwargs)
        user.set_password(password)
        user.save()
        return user


class AdminUserFactory(UserFactory):
    username = Faker("user_name")
    email = Faker("email")
    is_staff = True
    is_superuser = True
    first_name = Faker("first_name")
    last_name = Faker("last_name")


class TournamentsFactory(DjangoModelFactory):
    class Meta:
        model = Tournaments

    name = Faker("text")
    tournament_status = Faker("text")
    avoid_same_institution = Faker("boolean")
    missing_feedbacks = Faker("boolean")
    minimum_panel_score = Faker("random_int")
    check_in = Faker("boolean")
    start_date = Faker("date_object")
    end_date = Faker("date_object")
    creator = SubFactory("users.tests.factories.UserFactory")
    


class UsertournamentFactory(DjangoModelFactory):
    class Meta:
        model = Usertournament

    user = SubFactory("users.tests.factories.UserFactory")
    tournament = SubFactory(TournamentsFactory)
    role = Faker("text")
