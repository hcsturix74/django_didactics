from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Subject(models.Model):
    """
    Subject class - inherits from Model
    """
    subject_name = models.CharField(verbose_name=_('Subject Name'), max_length=100)
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)

    def __unicode__(self):
        return self.subject_name


class Course(models.Model):
    """
    Course class - inherits from Model
    """
    course_name = models.CharField(verbose_name=_('Course Name'), max_length=100)
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    subject = models.ForeignKey(Subject)
    #TODO: Add tagging here, at course level, not lesson
    #tags =

    def __unicode__(self):
        return self.course_name


class Lesson(models.Model):
    """
    Lesson class - inherits from Model
    """
    title = models.CharField(verbose_name=_('Lesson Title'), max_length=100)
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return self.title


class AttachmentType(models.Model):
    """
    AttachmentType class - inherits from Model
    Attachment type refers to different possible attachment for a lesson:
    - Presentations & Lessons
    - Exercises & Homeworks
    - Tests & Classworks
	- Solutions of exam exercices
    """
    type_name = models.CharField(verbose_name=_('Type Name'), max_length=100)
    #slug = models.SlugField(verbose_name=_('Type Name'), help_text=_('Automatically prepopulated. It will be used for folder names'))
    def __unicode__(self):
        return self.type_name


class LessonAttachment(models.Model):
    """
    LessonAttachment class - inherits from Model
    """
    caption = models.CharField(verbose_name=_('Caption'), max_length=100)
    attachment_type = models.ForeignKey(AttachmentType)
    attachment = models.FileField(verbose_name=_('Attachment'), upload_to='attachments/')
    lesson = models.ForeignKey(Lesson)

	
    def __unicode__(self):
        return self.caption
