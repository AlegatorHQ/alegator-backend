from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Model representing the user of the system.

    This is identical to Django's default user model,
    but is easier to modify in the future if needed.
    """

    # Make username optional and use email as primary identifier
    username = models.CharField(
        max_length=150,
        unique=True,
        null=True,
        blank=True,
    )
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def save(self, *args, **kwargs):
        if not self.username:
            # Generate a unique username if none provided
            import uuid

            self.username = f"user_{uuid.uuid4().hex[:8]}"
        super().save(*args, **kwargs)
