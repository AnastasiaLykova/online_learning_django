from django.contrib import admin

from course.models import Lesson, Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'preview', 'description')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'lesson_url','course')
    list_filter = ('name',)
    search_fields = ('name',)
