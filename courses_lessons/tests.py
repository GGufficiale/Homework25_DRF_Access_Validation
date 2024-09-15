from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from courses_lessons.models import Lesson, Course, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        # self.superuser = get_user_model().objects.create_superuser(email='django@mail.ru')
        self.user = User.objects.create(email='django@mail.ru', is_staff=True, is_superuser=True)
        self.course = Course.objects.create(name='course_test')
        self.lesson = Lesson.objects.create(name='lesson_test', description='test description')
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        """Тест на просмотр урока"""
        url = reverse("courses_lessons:lesson_get", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_lesson_create(self):
        """Тест на создание урока"""
        url = reverse("courses_lessons:lesson_create")
        data = {
            "name": "Test",
            "description": "Test description",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        """Тест на апдейт данных урока"""
        url = reverse("courses_lessons:lesson_update", args=(self.lesson.pk,))
        data = {
            "name": "Test update",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Test update")

    def test_lesson_delete(self):
        url = reverse("courses_lessons:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("courses_lessons:lesson_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lesson.objects.all().count(), 1)


class SubscriptionTestCase(APITestCase):
    """Тест функционала работы подписки на обновления курса"""

    def setUp(self):
        self.user = User.objects.create(email="apitest@apitest.com")
        self.course = Course.objects.create(name="Test Course", description="Test Course description")
        self.subscription = Subscription.objects.create(user=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        url = reverse("courses_lessons:course_subscribe")
        data = {
            "user": self.user.pk,
            "course": self.course.pk,
        }
        response = self.client.post(url, data)
        response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"message": "Подписка отключена"})
