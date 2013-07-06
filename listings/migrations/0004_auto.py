# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field dances on 'Organization'
        m2m_table_name = db.shorten_name(u'listings_organization_dances')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organization', models.ForeignKey(orm[u'listings.organization'], null=False)),
            ('dance', models.ForeignKey(orm[u'listings.dance'], null=False))
        ))
        db.create_unique(m2m_table_name, ['organization_id', 'dance_id'])


    def backwards(self, orm):
        # Removing M2M table for field dances on 'Organization'
        db.delete_table(db.shorten_name(u'listings_organization_dances'))


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
        }
    }

    complete_apps = ['listings']