# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Repeat'
        db.create_table(u'listings_repeat', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
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

        # Deleting field 'Event.id'
        db.delete_column(u'listings_event', u'id')

        # Adding field 'Event.repeat'
        db.add_column(u'listings_event', 'repeat',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['listings.Repeat'], unique=True, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Repeat'
        db.delete_table(u'listings_repeat')

        # Adding field 'Event.id'
        db.add_column(u'listings_event', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True),
                      keep_default=False)

        # Deleting field 'Event.repeat'
        db.delete_column(u'listings_event', 'repeat_id')


    models = {
        u'listings.dance': {
            'Meta': {'object_name': 'Dance'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'listings.event': {
            'Meta': {'object_name': 'Event'},
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['listings.Organization']"}),
            'repeat': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['listings.Repeat']", 'unique': 'True', 'primary_key': 'True'}),
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
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'friday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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