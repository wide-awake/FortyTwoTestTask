# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HttpRequest'
        db.create_table(u'activity_httprequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('server_protocol', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('status_code', self.gf('django.db.models.fields.IntegerField')()),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content_len', self.gf('django.db.models.fields.IntegerField')()),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'activity', ['HttpRequest'])


    def backwards(self, orm):
        # Deleting model 'HttpRequest'
        db.delete_table(u'activity_httprequest')


    models = {
        u'activity.httprequest': {
            'Meta': {'ordering': "['-priority', '-date']", 'object_name': 'HttpRequest'},
            'content_len': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'server_protocol': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'status_code': ('django.db.models.fields.IntegerField', [], {}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['activity']