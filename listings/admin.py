from django.contrib import admin
from listings.models import Organization, Event, Dance


class EventInline(admin.StackedInline):
    model = Event


class OrganizationAdmin(admin.ModelAdmin):
    inlines = [EventInline]


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Dance)