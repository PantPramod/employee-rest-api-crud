from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Employee(models.Model):

    class genderType(models.TextChoices):
        select = '', _('select...')
        male = 'male', _('Male')
        female = 'female', _('Female')

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    resume = models.FileField(upload_to='static/')
    email = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=100, choices=genderType.choices, default=genderType.select)
    linkedin = models.CharField(max_length=100)
    github = models.CharField(max_length=100)

    def __str__(self):
        return (self.name + " || " + self.email + " || " + self.phone + " || " + self.gender + " || " + self.linkedin + " || " + self.github)
