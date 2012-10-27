# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Error'
        db.create_table('js_log_error', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hexdigest', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('first_happened', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_happened', self.gf('django.db.models.fields.DateTimeField')()),
            ('details', self.gf('django.db.models.fields.TextField')()),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('js_log', ['Error'])


    def backwards(self, orm):
        # Deleting model 'Error'
        db.delete_table('js_log_error')


    models = {
        'js_log.error': {
            'Meta': {'object_name': 'Error'},
            'details': ('django.db.models.fields.TextField', [], {}),
            'first_happened': ('django.db.models.fields.DateTimeField', [], {}),
            'hexdigest': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_happened': ('django.db.models.fields.DateTimeField', [], {}),
            'number': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['js_log']