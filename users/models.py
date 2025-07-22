import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    supabase_id = models.UUIDField(unique=True, editable=False, null=True)

    def __str__(self):
        return self.username 