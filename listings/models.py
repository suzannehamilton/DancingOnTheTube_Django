from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Event(models.Model):
    organization = models.ForeignKey(Organization)

    def __unicode__(self):
        return self.organization.name