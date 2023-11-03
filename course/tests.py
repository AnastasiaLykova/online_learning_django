from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Lesson


class LessonTestCase(APITestCase):

    def setUp(self):
        self.lesson = Lesson.objects.create(
            name='test lesson',
            description='test lesson',
        )

    def test_lesson_list(self):

        response = self.client.get(
            reverse('course:lesson_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': 4, 'name': 'test lesson', 'preview': None, 'description': 'test lesson', 'lesson_url': None,
                 'course': None, 'creator': None}]}
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_create_lesson(self):

        data = {
            "name": "test lesson",
            "description": "test lesson"
        }

        response = self.client.post(
            reverse('course:lesson_create'),
            data=data
        )

        self.assertTrue(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_lesson_retrieve(self):

        response = self.client.get(
            f'/lesson/{self.lesson.id}/'
        )

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_lesson_update(self):

        data = {
            "name": "test lesson update"
        }

        response = self.client.put(
            f'/lesson/update/{self.lesson.id}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_lesson_delete(self):

        response = self.client.delete(
            f'/lesson/delete/{self.lesson.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Lesson.objects.all().exists()
        )

    def tearDown(self) -> None:
        self.lesson.delete()
