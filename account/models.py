from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    date_of_birth = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Profile of {self.user.username}'