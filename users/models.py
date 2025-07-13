from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Model representing the user of the system.

    This is identical to Django's default user model,
    but is easier to modify in the future if needed.
    """

    pass
