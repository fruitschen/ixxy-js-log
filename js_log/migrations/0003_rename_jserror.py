# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_table('js_log_error', 'js_log_jserror')


    def backwards(self, orm):
        db.rename_table('js_log_jserror','js_log_error')  

    models = {
        'js_log.jserror': {
            'Meta': {'object_name': 'JSError'},
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