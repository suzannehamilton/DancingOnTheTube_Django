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
    REPEAT = (
        ('NONE', 'None'),
        ('MONTH', 'Monthly'),
        ('WEEKLY', 'Weekly')
    )

    event = models.ForeignKey(Event, primary_key=True)
    frequency = models.CharField(max_length=1, choices=REPEAT)
    nth_day = models.IntegerField()
    n_weeks = models.IntegerField()

    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    sunday = models.BooleanField()