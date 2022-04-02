from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User # The user model for user authentication


class Idea(models.Model):
    """
        Idea Model where all details about the user's idea is stored
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    idea_id = models.UUIDField( verbose_name="Idea ID", primary_key=True, default=uuid4(), unique=True, editable=False, blank=False, null=False)
    title = models.CharField(max_length=500, unique=True, blank=False, null=False, editable=True)
    details = models.TextField(unique=True, null=False, editable=False, blank=False)
    date_time_created = models.DateTimeField(verbose_name="Date and time created", auto_now=True, editable=False)
    tags = models.JSONField()
    repository_link = models.TextField(unique=True, blank=True, null=True)

    def __repr__(self):
        return f"Project: {self.title} by {self.owner.username}"

