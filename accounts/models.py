from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class Account(AbstractUser):
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
    )
    email = models.CharField(max_length=100, unique=True)
