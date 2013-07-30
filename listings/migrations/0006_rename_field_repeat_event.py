# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_column(u'listings_repeat', 'repeat_id', 'event_id')

    def backwards(self, orm):
        db.rename_column(u'listings_repeat', 'event_id', 'repeat_id')


    models = {
        u'listings.dance': {
            'Meta': {'object_name': 'Dance'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'listings.event': {
            'Meta': {'object_name': 'Event'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['listings.Organization']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        u'listings.organization': {
            'Meta': {'object_name': 'Organization'},
            'dances': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['listings.Dance']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'listings.repeat': {
            'Meta': {'object_name': 'Repeat'},
            'event': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['listings.Event']", 'unique': 'True', 'primary_key': 'True'}),
            'frequency': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '10'}),
            'friday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'monday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'n_weeks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nth_day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'saturday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sunday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thursday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tuesday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wednesday': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['listings']