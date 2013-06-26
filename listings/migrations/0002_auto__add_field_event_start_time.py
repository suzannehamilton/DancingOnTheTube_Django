# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.start_time'
        db.add_column(u'listings_event', 'start_time',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.time(0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.start_time'
        db.delete_column(u'listings_event', 'start_time')


    models = {
        u'listings.event': {
            'Meta': {'object_name': 'Event'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['listings.Organization']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        u'listings.organization': {
            'Meta': {'object_name': 'Organization'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['listings']