from django import template
import settings
from didactics.models import Lesson, Course
 
register = template.Library()


@register.inclusion_tag('tt-lessons-by-course.html')
def show_lessons_by_course(course_id):
    """
    This template tag shows all the lesson of a specific course
    course_id - Course id to be used to retrieve all associated lessons  
    """
    
    lssns_list = Lesson.objects.filter(course=course_id)
    return {
        'lessons': lssns_list,
    }

    
@register.inclusion_tag('tt-courses-list.html')
def show_courses_list():
    """
    This template tag shows all the courses
    """
    
    courses_list = Course.objects.all()
    return {
        'courses': courses_list,
    }
