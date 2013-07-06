from django.db import models


class Dance(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=200)
    dances = models.ManyToManyField(Dance)

    def __unicode__(self):
        return self.name


class Event(models.Model):
    organization = models.ForeignKey(Organization)
    start_time = models.TimeField()

    def __unicode__(self):
        return self.organization.name