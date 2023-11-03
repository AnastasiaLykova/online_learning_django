from rest_framework import serializers

from course.models import Course, Lesson
from course.validators import YoutubeValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [YoutubeValidator('lesson_url')]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


    def get_lesson_count(self, instance):
        return instance.lesson_set.count()
