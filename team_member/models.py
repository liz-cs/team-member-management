from django.db import models

# Create your models here.

role_status = ((False, "Regular - Can't delete team members"), (True, "Admin - Can delete team members"))


class TeamMember(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    status = models.BooleanField(default=False, choices=role_status)

    def __str__(self):
        if self.status:
            return self.first_name + ' ' + self.last_name + ' (admin)'
        else:
            return self.first_name + ' ' + self.last_name
