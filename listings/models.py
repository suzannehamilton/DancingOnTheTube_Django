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


class Repeat(models.Model):
    event = models.OneToOneField(Event, primary_key=True)

    NONE = 'NONE'
    MONTHLY = 'MONTHLY'
    WEEKLY = 'WEEKLY'

    REPEAT = (
        (NONE, 'None'),
        (MONTHLY, 'Monthly'),
        (WEEKLY, 'Weekly')
    )

    frequency = models.CharField(max_length=10, choices=REPEAT, default=NONE)
    nth_day = models.IntegerField(null=True, blank=True)
    n_weeks = models.IntegerField(null=True, blank=True)

    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    sunday = models.BooleanField()