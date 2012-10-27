# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Error.short_message'
        db.add_column('js_log_error', 'short_message',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=128, blank=True),
                      keep_default=False)

        # Adding field 'Error.user_agent'
        db.add_column('js_log_error', 'user_agent',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=256, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Error.short_message'
        db.delete_column('js_log_error', 'short_message')

        # Deleting field 'Error.user_agent'
        db.delete_column('js_log_error', 'user_agent')


    models = {
        'js_log.error': {
            'Meta': {'object_name': 'Error'},
            'details': ('django.db.models.fields.TextField', [], {}),
            'first_happened': ('django.db.models.fields.DateTimeField', [], {}),
            'hexdigest': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_happened': ('django.db.models.fields.DateTimeField', [], {}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'short_message': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        }
    }

    complete_apps = ['js_log']