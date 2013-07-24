# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Repeat'
        db.create_table(u'listings_repeat', (
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['listings.Event'], primary_key=True)),
            ('frequency', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('nth_day', self.gf('django.db.models.fields.IntegerField')()),
            ('n_weeks', self.gf('django.db.models.fields.IntegerField')()),
            ('monday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tuesday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('wednesday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('thursday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('friday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('saturday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sunday', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'listings', ['Repeat'])


    def backwards(self, orm):
        # Deleting model 'Repeat'
        db.delete_table(u'listings_repeat')


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
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['listings.Event']", 'primary_key': 'True'}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'friday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'monday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'n_weeks': ('django.db.models.fields.IntegerField', [], {}),
            'nth_day': ('django.db.models.fields.IntegerField', [], {}),
            'saturday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sunday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thursday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tuesday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wednesday': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['listings']