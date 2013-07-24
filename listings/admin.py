from django.contrib import admin
from listings.models import Organization, Event, Dance, Repeat


class EventInline(admin.StackedInline):
    model = Event


class OrganizationAdmin(admin.ModelAdmin):
    inlines = [EventInline]


class ScheduleInline(admin.StackedInline):
    model = Repeat


class EventAdmin(admin.ModelAdmin):
    inlines = [ScheduleInline]

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Dance)
admin.site.register(Event, EventAdmin)