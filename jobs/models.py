from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User


class Job (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class PersonalJob(Job):
    user = models.ForeignKey(User, on_delete=models.CASCADE)