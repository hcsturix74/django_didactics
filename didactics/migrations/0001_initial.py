# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subject'
        db.create_table(u'didactics_subject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'didactics', ['Subject'])

        # Adding model 'Course'
        db.create_table(u'didactics_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['didactics.Subject'])),
        ))
        db.send_create_signal(u'didactics', ['Course'])

        # Adding model 'Lesson'
        db.create_table(u'didactics_lesson', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['didactics.Course'])),
        ))
        db.send_create_signal(u'didactics', ['Lesson'])

        # Adding model 'AttachmentType'
        db.create_table(u'didactics_attachmenttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'didactics', ['AttachmentType'])

        # Adding model 'LessonAttachment'
        db.create_table(u'didactics_lessonattachment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('attachment_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['didactics.AttachmentType'])),
            ('attachment', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('lesson', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['didactics.Lesson'])),
        ))
        db.send_create_signal(u'didactics', ['LessonAttachment'])


    def backwards(self, orm):
        # Deleting model 'Subject'
        db.delete_table(u'didactics_subject')

        # Deleting model 'Course'
        db.delete_table(u'didactics_course')

        # Deleting model 'Lesson'
        db.delete_table(u'didactics_lesson')

        # Deleting model 'AttachmentType'
        db.delete_table(u'didactics_attachmenttype')

        # Deleting model 'LessonAttachment'
        db.delete_table(u'didactics_lessonattachment')


    models = {
        u'didactics.attachmenttype': {
            'Meta': {'object_name': 'AttachmentType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'didactics.course': {
            'Meta': {'object_name': 'Course'},
            'course_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['didactics.Subject']"})
        },
        u'didactics.lesson': {
            'Meta': {'object_name': 'Lesson'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['didactics.Course']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'didactics.lessonattachment': {
            'Meta': {'object_name': 'LessonAttachment'},
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'attachment_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['didactics.AttachmentType']"}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['didactics.Lesson']"})
        },
        u'didactics.subject': {
            'Meta': {'object_name': 'Subject'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['didactics']