from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Employee(models.Model):

    class genderType(models.TextChoices):
        male = 'male', _('Male')
        female = 'female', _('Female')

    name = models.CharField(max_length=100, help_text="Name of Employee")
    phone = models.CharField(max_length=100, help_text="Phone Number")
    resume = models.FileField(upload_to='static/', help_text="Resume File")
    email = models.CharField(max_length=100, help_text="Email Id")
    gender = models.CharField(
        max_length=100, choices=genderType.choices, help_text="male or female")
    linkedin = models.CharField(max_length=100, help_text="linked in url")
    github = models.CharField(max_length=100, help_text="github url")

    def __str__(self):
        return (self.name + " || " + self.email + " || " + self.phone + " || " + self.gender + " || " + self.linkedin + " || " + self.github)
