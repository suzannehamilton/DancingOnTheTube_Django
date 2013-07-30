from django import forms
from django.contrib import admin
from listings.models import Organization, Event, Dance, Repeat
from django.forms.models import inlineformset_factory


class EventInline(admin.StackedInline):
    model = Event


class OrganizationAdmin(admin.ModelAdmin):
    inlines = [EventInline]


class RepeatForm(forms.models.BaseInlineFormSet):
    class Meta:
        model = Repeat

    def clean(self):
        try:
            forms = [f for f in self.forms
                       if  f.cleaned_data
                       # This next line filters out inline objects that did exist
                       # but will be deleted if we let this form validate --
                       # obviously we don't want to count those if our goal is to
                       # enforce a min or max number of related objects.
                       and not f.cleaned_data.get('DELETE', False)]
            cleaned_data = forms[0].cleaned_data
            # data = self.form.clean()
            #
            # if self.instance.parent_foo == 'bar':
            a = 3
                # if len(forms) == 0:
                #     raise forms.ValidationError(""" If the parent object's 'foo' is
                #     'bar' then it needs at least one related object! """)
        except AttributeError:
            pass


class ScheduleInline(admin.StackedInline):
    model = Repeat
    formset = RepeatForm



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['start_time', 'organization']

    # def clean(self):
    #     form_data = self.data
    #
    #     cleaned_data = super(EventForm, self).clean()
    #     frequency = form_data.get("repeat-0-frequency")
    #     nth_day = form_data.get("repeat-0-nth_day")
    #
    #     if frequency == Repeat.NONE:
    #         message = u"You cannot give details of recurrences if the event is not repeated"
    #         if nth_day:
    #             self._errors["repeat-0-frequency"] = self.error_class([message])
    #             self._errors["repeat-0-nth_day"] = self.error_class([message])
    #             raise forms.ValidationError(message)
    #
    #     return form_data



class InlineAdmin(admin.TabularInline):
    model = Event.repeat
    formset = RepeatForm


class EventAdmin(admin.ModelAdmin):
    inlines = [ScheduleInline]
    form = EventForm

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Dance)
admin.site.register(Event, EventAdmin)