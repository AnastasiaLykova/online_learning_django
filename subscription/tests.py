from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from course.models import Course
from subscription.models import Subscription
from users.models import User


class SubscriptionTestCase(TestCase):

    def setUp(self):
        self.course = Course.objects.create(
            name='test course',
            description='test description',
        )
        self.user = User.objects.create(
            email='test@test',
        )
        self.subscription = Subscription.objects.create(
            user=self.user,
            course=self.course,
        )

    def test_subscription_list(self):

        response = self.client.get(
            reverse('subscription:list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{'id': 4, 'is_subscribed': False, 'user': 3, 'course': 3}]
        )

        self.assertTrue(
            Subscription.objects.all().exists()
        )

    def test_subscription_create(self):
        data = {
            'user': self.user.id,
            'course': self.course.id,
        }

        response = self.client.post(
            reverse('subscription:create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Subscription.objects.all().exists()
        )

    def test_subscription_delete(self):
        response = self.client.delete(
            f'/subscription/delete/{self.subscription.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Subscription.objects.all().exists()
        )

    def tearDown(self):
        self.course.delete()
        self.user.delete()
        self.subscription.delete()
