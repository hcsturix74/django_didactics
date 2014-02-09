# Create your views here.
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView 
from django.utils import timezone
from didactics.models import Lesson, Course, LessonAttachment

class LessonDetailView(DetailView):
    """
    LessonDetailView class - inherits from DetailView
    This view shows lesson with all related attachments.
    """
    model = Lesson

    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context

        
        
class LessonListView(ListView):
    """
    LessonListView class - inherits from ListView
    This view shows lesson list in a table.
    """
    model = Lesson
    
    def get_context_data(self, **kwargs):
        context = super(LessonListView, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context
        
        
class CourseListView(ListView):
    """
    CourseListView class - inherits from ListView
    This view shows course list in a table.
    """
    model = Course
    
    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context