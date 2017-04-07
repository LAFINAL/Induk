# from django.conf import settings
from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.signals import user_logged_in
from report.models import Board


class User(AbstractUser):
	signup_approved = models.BooleanField(default=False)
	company = models.ManyToManyField(Board, related_name='user_set')


