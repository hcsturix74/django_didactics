#from django.db import models
#from django.contrib.auth.models import User
from django.contrib import admin
from didactics.models import *

class AuthorSavingMixin(object):

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

class SubjectAdmin(AuthorSavingMixin, admin.ModelAdmin):
    """
    SubjectAdmin
    """
    search_fields = ('subject_name', )
    list_display = ('subject_name', )

admin.site.register(Subject, SubjectAdmin)


class CourseAdmin(AuthorSavingMixin, admin.ModelAdmin):
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
    extra = 1



class AttachmentTypeAdmin(AuthorSavingMixin, admin.ModelAdmin):
    """
    AttachmentType
    """
    list_display = ('type_name',)
    search_fields = ('type_name',)


admin.site.register(AttachmentType, AttachmentTypeAdmin)


class LessonAdmin(AuthorSavingMixin, admin.ModelAdmin):
    """
    LessonAdmin
    """
    list_display = ('title', 'course', 'subject',)
    search_fields = ('title', 'course',)
    exclude = ('author',)
    inlines = [LessonAttachmentInline]


    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in filter(lambda obj: isinstance(obj, LessonAttachment), instances):
             if instance.__dict__.get('author', None) is None:
                 instance.author = request.user
                 instance.save()
        formset.save_m2m()

admin.site.register(Lesson, LessonAdmin)
