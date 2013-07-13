# -*- coding: utf-8 -*-
from south.v2 import DataMigration
from django.template.defaultfilters import slugify

class Migration(DataMigration):

    def forwards(self, orm):
        for calendar in orm['schedule.Calendar'].objects.all():
            if not calendar.slug:
                calendar.slug = slugify(calendar.name)
                calendar.save()

    def backwards(self, orm):
        "No backwards migration, because we can't identify previously-created slugs"

    models = {
        u'listings.dance': {
            'Meta': {'object_name': 'Dance'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'listings.organization': {
            'Meta': {'object_name': 'Organization'},
            'calendar': ('annoying.fields.AutoOneToOneField', [], {'to': "orm['schedule.Calendar']", 'unique': 'True'}),
            'dances': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['listings.Dance']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'schedule.calendar': {
            'Meta': {'object_name': 'Calendar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['listings']
    symmetrical = True
