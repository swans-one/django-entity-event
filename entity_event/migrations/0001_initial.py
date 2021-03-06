# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Medium'
        db.create_table(u'entity_event_medium', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'entity_event', ['Medium'])

        # Adding model 'Source'
        db.create_table(u'entity_event_source', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entity_event.SourceGroup'])),
        ))
        db.send_create_signal(u'entity_event', ['Source'])

        # Adding model 'SourceGroup'
        db.create_table(u'entity_event_sourcegroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'entity_event', ['SourceGroup'])

        # Adding model 'Unsubscription'
        db.create_table(u'entity_event_unsubscription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entity.Entity'])),
            ('medium', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entity_event.Medium'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entity_event.Source'])),
        ))
        db.send_create_signal(u'entity_event', ['Unsubscription'])

        # Adding model 'Subscription'
        db.create_table(u'entity_event_subscription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('medium', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entity_event.Medium'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entity_event.Source'])),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entity.Entity'])),
            ('sub_entity_kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entity.EntityKind'], null=True)),
            ('only_following', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'entity_event', ['Subscription'])

        # Adding model 'Event'
        db.create_table(u'entity_event_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entity_event.Source'])),
            ('context', self.gf('jsonfield.fields.JSONField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('time_expires', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal(u'entity_event', ['Event'])

        # Adding model 'EventActor'
        db.create_table(u'entity_event_eventactor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entity_event.Event'])),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entity.Entity'])),
        ))
        db.send_create_signal(u'entity_event', ['EventActor'])

        # Adding model 'EventSeen'
        db.create_table(u'entity_event_eventseen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entity_event.Event'])),
            ('medium', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entity_event.Medium'])),
            ('time_seen', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow)),
        ))
        db.send_create_signal(u'entity_event', ['EventSeen'])


    def backwards(self, orm):
        # Deleting model 'Medium'
        db.delete_table(u'entity_event_medium')

        # Deleting model 'Source'
        db.delete_table(u'entity_event_source')

        # Deleting model 'SourceGroup'
        db.delete_table(u'entity_event_sourcegroup')

        # Deleting model 'Unsubscription'
        db.delete_table(u'entity_event_unsubscription')

        # Deleting model 'Subscription'
        db.delete_table(u'entity_event_subscription')

        # Deleting model 'Event'
        db.delete_table(u'entity_event_event')

        # Deleting model 'EventActor'
        db.delete_table(u'entity_event_eventactor')

        # Deleting model 'EventSeen'
        db.delete_table(u'entity_event_eventseen')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'entity.entity': {
            'Meta': {'unique_together': "(('entity_id', 'entity_type', 'entity_kind'),)", 'object_name': 'Entity'},
            'display_name': ('django.db.models.fields.TextField', [], {'db_index': 'True', 'blank': 'True'}),
            'entity_id': ('django.db.models.fields.IntegerField', [], {}),
            'entity_kind': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entity.EntityKind']", 'on_delete': 'models.PROTECT'}),
            'entity_meta': ('jsonfield.fields.JSONField', [], {'null': 'True'}),
            'entity_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'on_delete': 'models.PROTECT'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'})
        },
        u'entity.entitykind': {
            'Meta': {'object_name': 'EntityKind'},
            'display_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256', 'db_index': 'True'})
        },
        u'entity_event.event': {
            'Meta': {'object_name': 'Event'},
            'context': ('jsonfield.fields.JSONField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entity_event.Source']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time_expires': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'entity_event.eventactor': {
            'Meta': {'object_name': 'EventActor'},
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entity.Entity']"}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entity_event.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'entity_event.eventseen': {
            'Meta': {'object_name': 'EventSeen'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entity_event.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medium': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entity_event.Medium']"}),
            'time_seen': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'})
        },
        u'entity_event.medium': {
            'Meta': {'object_name': 'Medium'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'entity_event.source': {
            'Meta': {'object_name': 'Source'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entity_event.SourceGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'entity_event.sourcegroup': {
            'Meta': {'object_name': 'SourceGroup'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'entity_event.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entity.Entity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medium': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entity_event.Medium']"}),
            'only_following': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entity_event.Source']"}),
            'sub_entity_kind': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entity.EntityKind']", 'null': 'True'})
        },
        u'entity_event.unsubscription': {
            'Meta': {'object_name': 'Unsubscription'},
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entity.Entity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medium': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entity_event.Medium']"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entity_event.Source']"})
        }
    }

    complete_apps = ['entity_event']