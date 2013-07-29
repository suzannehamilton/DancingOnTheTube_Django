from django import forms
from django.contrib import admin
from listings.models import Organization, Event, Dance, Repeat


class EventInline(admin.StackedInline):
    model = Event


class OrganizationAdmin(admin.ModelAdmin):
    inlines = [EventInline]


class ScheduleInline(admin.StackedInline):
    model = Repeat


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['start_time', 'organization']

    def clean(self):
        form_data = self.data
        cleaned_data = super(EventForm, self).clean()
        frequency = form_data.get("repeat-0-frequency")
        nth_day = form_data.get("repeat-0-nth_day")

        if frequency == Repeat.NONE:
            if nth_day:
                raise forms.ValidationError("Nth day cannot be checked if event is not repeated")

        return cleaned_data


class EventAdmin(admin.ModelAdmin):
    inlines = [ScheduleInline]
    form = EventForm

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Dance)
admin.site.register(Event, EventAdmin)