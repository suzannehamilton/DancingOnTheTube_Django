from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=200)


class Event(models.Model):
    organization = models.ForeignKey(Organization)