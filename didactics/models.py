from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from didactics.managers import PublicManager
import datetime

class GenericBaseModel(models.Model):
    """
    GenericBaseModel class - inherits from models.Model
    This class is an abstract structure for a basic model for this app
    """
    is_public = models.BooleanField(blank=True, default=True, verbose_name=_('Is public'))
    author =  models.ForeignKey(User, verbose_name=_('Author'), blank=True, null=True)
    created = models.DateTimeField(verbose_name=_('Creation Date'), default=datetime.datetime.now())
    updated = models.DateTimeField(verbose_name=_('Modify Date'), default=datetime.datetime.now())
    objects = models.Manager()
    pub_objects = PublicManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        This is the overridden save method
        """
        if not self.id:
            self.created = datetime.datetime.now()
        self.updated = datetime.datetime.now()
        super(GenericBaseModel, self).save(*args, **kwargs)

    def get_history(self):
        """
        This method retrieves the history for this object searching in LogEntry Table
        """
        lst = []
        try:
            lst = LogEntry.objects.filter(content_type=ContentType.objects.get_for_model(self).id, object_id=self.pk)
        except Exception:
            pass
        return lst

    def _get_creation_date(self):
        """
        This method retrieves the creation date for this object
        """
        return self.created

    creation_date = property(_get_creation_date)

    def _get_modify_date(self):
        """
        This method retrieves the modification date for this object
        """
        return self.updated

    modify_date = property(_get_modify_date)

class Subject(GenericBaseModel):
    """
    Subject class - inherits from Model
    """
    subject_name = models.CharField(verbose_name=_('Subject Name'), max_length=100)
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)

    def __unicode__(self):
        return self.subject_name


class Course(GenericBaseModel):
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


class Lesson(GenericBaseModel):
    """
    Lesson class - inherits from Model
    """
    title = models.CharField(verbose_name=_('Lesson Title'), max_length=100)
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return self.title

    def subject(self):
        return self.course.subject
    subject.admin_order_field  = 'lesson__subject'


class AttachmentType(GenericBaseModel):
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


class LessonAttachment(GenericBaseModel):
    """
    LessonAttachment class - inherits from Model
    """
    caption = models.CharField(verbose_name=_('Caption'), max_length=100)
    attachment_type = models.ForeignKey(AttachmentType)
    attachment = models.FileField(verbose_name=_('Attachment'), upload_to='attachments/')
    lesson = models.ForeignKey(Lesson, verbose_name=_('Lesson'))

	
    def __unicode__(self):
        return self.caption
