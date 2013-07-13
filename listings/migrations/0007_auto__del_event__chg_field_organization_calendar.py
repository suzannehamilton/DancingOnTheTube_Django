# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'listings_event')


        # Changing field 'Organization.calendar'
        db.alter_column(u'listings_organization', 'calendar_id', self.gf('annoying.fields.AutoOneToOneField')(default=0, to=orm['schedule.Calendar'], unique=True))

    def backwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'listings_event', (
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['listings.Organization'])),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'listings', ['Event'])


        # Changing field 'Organization.calendar'
        db.alter_column(u'listings_organization', 'calendar_id', self.gf('annoying.fields.AutoOneToOneField')(to=orm['schedule.Calendar'], unique=True, null=True))

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