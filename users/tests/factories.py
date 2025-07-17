from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory
import factory

User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("email",)

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    is_active = True

    @staticmethod
    def with_password(password, **kwargs):
        user = UserFactory.build(**kwargs)
        user.set_password(password)
        user.save()
        return user


class AdminUserFactory(UserFactory):
    username = factory.Sequence(lambda n: f"admin{n}")
    email = factory.Faker("email")
    is_staff = True
    is_superuser = True
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
