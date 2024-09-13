from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from courses_lessons.models import Lesson, Course
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='django@mail.ru')
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
