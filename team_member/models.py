import datetime

from django.db import models

# Create your models here.
from django.utils import timezone


class TeamMember(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    def __str__(self):
        if self.status:
            return self.first_name + ' ' + self.last_name + ' (admin)'
        else:
            return self.first_name + ' ' + self.last_name
