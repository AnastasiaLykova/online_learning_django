from django.shortcuts import render
from rest_framework import viewsets, generics
from course.models import Course, Lesson
from course.paginations import CoursePaginator
from course.permissions import IsCreator, IsModerator
from course.serializers import CourseSerializer, LessonSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator

    def get_permissions(self):
        if self.request.method == 'DELETE':
            self.permission_classes = [IsAuthenticated, IsCreator]
        elif self.request.method == 'UPDATE':
            self.permission_classes = [IsAuthenticated, IsCreator | IsModerator]
        elif self.request.method == 'CREATE':
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        else:
            self.permission_classes = [IsAuthenticated, IsCreator | IsModerator]
        return super(CourseViewSet, self).get_permissions()

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.creator = self.request.user
        new_course.save()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
#    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.creator = self.request.user if self.request.user.is_authenticated else None
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
#    permission_classes = [IsAuthenticated, IsCreator | IsModerator]
    pagination_class = CoursePaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
#    permission_classes = [IsAuthenticated, IsCreator | IsModerator]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
#    permission_classes = [IsAuthenticated, IsCreator | IsModerator]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
#    permission_classes = [IsAuthenticated, IsCreator]
