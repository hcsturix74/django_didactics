#from django.db import models
#from django.contrib.auth.models import User
from django.contrib import admin
from didactics.models import *


class SubjectAdmin(admin.ModelAdmin):
    """
    SubjectAdmin
    """
    search_fields = ('subject_name', )
    list_display = ('subject_name', )

admin.site.register(Subject, SubjectAdmin)


class CourseAdmin(admin.ModelAdmin):
    """
    CourseAdmin
    """
    list_display = ('course_name', 'subject',)
    search_fields = ('course_name', 'subject',)

admin.site.register(Course, CourseAdmin)


class LessonAttachmentInline(admin.StackedInline):
    """
    LessonAttachmentInline
    """
    model = LessonAttachment
    extra = 2


class AttachmentTypeAdmin(admin.ModelAdmin):
    """
    AttachmentType
    """
    list_display = ('type_name',)
    search_fields = ('type_name',)


admin.site.register(AttachmentType, AttachmentTypeAdmin)


class LessonAdmin(admin.ModelAdmin):
    """
    LessonAdmin
    """
    list_display = ('title', 'course', )
    search_fields = ('title', 'course', )
    inlines = [LessonAttachmentInline]

admin.site.register(Lesson, LessonAdmin)
